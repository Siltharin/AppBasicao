from flask import Flask, Response, request, render_template
import pymongo


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
dburi = "mongodb+srv://appbasicuser:appbasicusert3st3@cluster0-jvnpg.mongodb.net/test?retryWrites=true"
	

@app.route('/')
def main():
	return render_template('index.html')
	
	
@app.route('/saveForm', methods=['POST'])
def saveForm():
	contact = request.args.get("contact")
	message = request.args.get("message")
	token = request.args.get("token")

	client = pymongo.MongoClient(dburi)
	db = client.test	
	messages = db.messages
	messages.insert_one({ "contact": contact, "message": message})

	return str(message)


@app.route('/listForm', methods=['POST'])
def listForm():	

	client = pymongo.MongoClient(dburi)
	db = client.test	
	messages = db.messages
	
	cursor = messages.find() 
	for item in cursor:
	    print(item["message"])
	return (str(cursor))
	