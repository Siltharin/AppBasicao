import pymongo
import json, datetime
from bson.json_util import dumps


dburi = "mongodb+srv://appbasicuser:appbasicusert3st3@cluster0-jvnpg.mongodb.net/test?retryWrites=true"
dbcollectionname = "messages"
	
def saveCadastro():
	token = request.args.get("token")
	item = {"contact": request.args.get("contact"), 
			"message": request.args.get("message"),
			"timestamp": datetime.datetime.utcnow()}

	client = pymongo.MongoClient(dburi)
	db = client.test	
	dbcollection = db[dbcollectionname]
	itemid = dbcollection.insert_one(item).inserted_id
	return str(itemid)


def listCadastro():	
	client = pymongo.MongoClient(dburi)
	db = client.test	
	dbcollection = db[dbcollectionname]	
	cursor = dbcollection.find().sort("timestamp", -1) 
	return dumps(cursor)
	