from flask import Flask, render_template
import pymongo


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def main():
	return render_template('index.html')
	
	
@app.route('/saveForm', methods=['POST'])
def saveForm():
	contact = request.args.get("contact")
	message = request.args.get("message")
	token = request.args.get("token")

	uri = "mongodb+srv://appbasicuser:appbasicusert3st3@cluster0-jvnpg.mongodb.net/test?retryWrites=true"
	client = pymongo.MongoClient(uri)
	db = client.test
	messages = db.messages
	#messages.insert_one({ "_id": 1,"name": "pizza", "calories": 266, "fats": {"saturated": 4.5, "trans": 0.2 },"protein": 11})
	cursor = messages.find()
 
	for item in cursor:
	    print(item["name"])
	return (str(cursor))
	