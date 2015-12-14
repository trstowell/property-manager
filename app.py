from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
import bson.json_util
import datetime
import json

client = MongoClient()
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'assets'
mongo = PyMongo(app)
cors = CORS(app)


@app.route('/<_id>')
def hello_world(_id):
    return 'Hello world'

@app.route('/users', methods=['GET'])
def users():
    """Returns all documents in the User collection"""

    cursor = mongo.db.users.find()

    docs = [doc for doc in cursor]

    return bson.json_util.dumps(docs)


@app.route('/user/<username>', methods=['GET'])
def user(username):
    """Returns the document for the supplied User"""

    doc = mongo.db.users.find_one_or_404({'username': username})

    return bson.json_util.dumps(doc)


@app.route('/places', methods=['GET'])
def places():
    """Returns all documents in the Places collection"""

    cursor = mongo.db.places.find()

    docs = [doc for doc in cursor]

    return bson.json_util.dumps(docs)


@app.route("/place/<_id>")
def place(_id):
    """Returns the document in the Place collection with the given ObjectId"""

    doc = mongo.db.places.find_one_or_404({'_id': ObjectId(_id)})

    return bson.json_util.dumps(doc)


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
