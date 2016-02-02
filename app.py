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


@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/currency/<currency_code>')
def currency(currency_code):

    doc = mongo.db.currencies.find_one_or_404({'currency_code': currency_code.upper()})

    return bson.json_util.dumps(doc)


@app.route('/user/<_id>', methods=['GET'])
def user(_id):
    """Returns the document in the Users collection with the given ObjectID """

    doc = mongo.db.users.find_one_or_404({'_id': ObjectId(_id)})

    return bson.json_util.dumps(doc)


@app.route("/booking/<_id>", methods=['GET', 'POST'])
def booking(_id):
    """Returns the document in the Booking collection with the given ObjectId"""

    doc = mongo.db.bookings.find_one_or_404({'_id': ObjectId(_id)})

    return bson.json_util.dumps(doc)


@app.route('/place/<_id>', methods=['GET'])
def place(_id):
    """Returns the document in the Places collection with the given ObjectID"""

    doc = mongo.db.places.find_one_or_404({'_id': ObjectId(_id)})

    return bson.json_util.dumps(doc)


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
