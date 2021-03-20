from flask import Flask, request, json, Response
from pymongo import MongoClient

app = Flask(__name__)

class MongoAPI:
    def __init__(self, data):
        self.client = MongoClient("mongodb://localhost:5000/")

        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
            documents = self.collection.find()
            output = [{item: data[item] for item in data if item != '_id'} for data in documents]
            return output


    def write(self, data):
        #log.info('Writing Data')
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                    'Document_ID': str(response.inserted_id)}
        return output
    

    def update(self):
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else 'Nothing was updated.'}
        return output


    def delete(self, data):
        filt = data['Document']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfuly Deleted' if response.deleted_count > 0 else 'Document not found.'}
        return output


# ENDPOINTS

@app.route('/')
def base():
    """ping"""
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')


@app.route('/pairs', methods=['GET'])
def get_pairs():
    """get all coin pairs"""
    data = {
        "database": "Binance",
        "collection": "pairs",
    }
    #data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.read()
    return Response(response=json.dumps(response, indent=4),
                    status=200,
                    mimetype='application/json')

    

if __name__ == '__main__':

    #app.run(debug=True, port=5001, host='0.0.0.0')

     # add pairs data to mongodb for testing
    with open('data/json/pairs.json') as f:
        file_data = json.load(f)

    client = MongoClient("mongodb://localhost:5000/")
    db = client["Binance"]
    col = db["pairs"]
    col.insert_one(file_data)
    app.run(debug=True, port=5001, host='0.0.0.0')

    