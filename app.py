from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
	{
		'name' : 'My Store',
		'items': [
			{
				'name': 'My Item',
				'price': 69.99
			}
		]
	}
]

@app.route('/store', methods=['POST'])
def create():
	request_data = request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)

@app.route('/store/<string:name>')
def retrieve(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return jsonify({'message': 'store not found'})	

@app.route('/store')
def list():
	return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item():
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def retrieve_item(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items': store['items']})
	return jsonify({'message': 'store not found'})

app.run(host='0.0.0.0')