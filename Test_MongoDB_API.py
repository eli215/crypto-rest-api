from flask import Flask, request, json, Response
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'mongodb'
app.config['MONGO_URI'] = 'mongodb://localhost:5000/'

mongo = PyMongo(app)

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


@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')

# route to get all coin pairs
@app.route('/pairs', methods=['GET'])
def get_pairs():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    respose = obj1.read()

    

if __name__ == '__main__':

    app.run(debug=True, port=5001, host='0.0.0.0')

    data = {
        "database": "MongoTest",
        "collection": "people",
    }

    data1 = {
        "database": "MongoTest",
        "collection": "people",
        "Document": {
            "First_Name": "Jhon",
            "Age": 50
    }
}

    mongo_obj = MongoAPI(data)
    mongo_obj.write(data1)
    print(json.dumps(mongo_obj.read(), indent=4))