import json
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'Binance'
app.config['MONGO_URI'] = 'mongodb://localhost:5000/Binance'

mongo = PyMongo(app)

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')


@app.route('/pairs', methods=['GET'])
def get_pairs():
    """get all crypto trading pairs"""
    pairs = mongo.db.pairs
    output = []
    for p in pairs.find():
        output.append({'id' : p['id'], 'symbol' : p['symbol']})
    return jsonify({'result' : output})


if __name__ == '__main__':
    
    # add test data to mongodb
    with open('data/json/pairs.json') as f:
        file_data = json.load(f)
    
    db = mongo.db
    #col_pairs = db['pairs']
    #db.create_collection('pairs')

    db.pairs.insert_one(file_data)

    # print pairs data
    #pairs = db['pairs']
    pairs = db.pairs.find()
    print(jsonify(pairs))

    app.run(debug=True, port=5001, host='0.0.0.0')