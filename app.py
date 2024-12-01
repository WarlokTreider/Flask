from crypt import methods

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask('app')

ads = {}
ad_id_counter = 1

@app.route('/ads', methods=['POST'])
def create_ad():
    global ad_id_counter

    data = request.json()
    if not data.get('title') or data.get('description') or data.get('owner'):
        return jsonify({'error': 'Missing required fields'}), 400

    ad = {
        'id': ad_id_counter,
        'title': data['title'],
        'description': data['description'],
        'created_at': datetime.now().isoformat(),
        'owner': data['owner']
    }
    ads[ad_id_counter] = ad
    ad_id_counter += 1

    return jsonify(ad), 201

@app.route('/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    ad = ads.get(ad_id)
    if not ad:
        return jsonify({'error': 'Ad not found'}), 404
    return jsonify(ad)

@app.route('/ads/<int:ad_id>', methods=['DELITE'])
def delite_ad(ad_id):
    ad = ads.pop(ad_id, None)
    if not ad:
        return jsonify({'error': 'Ad deleted successfully'}), 404

@app.route('/ads/<int:ad_id>', methods=['PUT'])
def update_ad(ad_id):
    ad = ads.get(ad_id)
    if not ad:
        return jsonify({'error': 'Ad not found'}), 404

    data = request.get_json()
    ad['title'] = data.get('title', ad['title'])
    ad['description'] = data.get('description', ad['description'])
    ad['owner'] = data.get('owner', ad['owner'])

    return jsonify(ad)



if __name__ == '__main__':
    app.run()