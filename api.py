from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'mongodb'
app.config['MONGO_URI'] = 'mongodb://localhost:5000/'

mongo = PyMongo(app)

@app.route('/pairs', methods=['GET'])
def get_pairs():
    """get all crypto trading pairs"""
    