from flask import Flask, Response, request, render_template
import pymongo
import json, datetime
from bson.json_util import dumps


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
	

@app.route('/')
def main():
	return render_template('index.html')
	

dburi = "mongodb+srv://appbasicuser:appbasicusert3st3@cluster0-jvnpg.mongodb.net/test?retryWrites=true"
dbcollectionname = "messages"
	
@app.route('/saveForm', methods=['POST'])
def saveForm():
	token = request.args.get("token")
	item = {"contact": request.args.get("contact"), 
			"message": request.args.get("message"),
			"timestamp": datetime.datetime.utcnow()}

	client = pymongo.MongoClient(dburi)
	db = client.test	
	dbcollection = db[dbcollectionname]
	itemid = dbcollection.insert_one(item).inserted_id
	return str(itemid)


@app.route('/listForm', methods=['POST'])
def listForm():	
	client = pymongo.MongoClient(dburi)
	db = client.test	
	dbcollection = db[dbcollectionname]	
	cursor = dbcollection.find().sort("timestamp", -1) 
	return dumps(cursor)
	