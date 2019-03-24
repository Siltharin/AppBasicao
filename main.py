from flask import Flask, render_template
import pymongo


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def main():
	return render_template('index.html')
	
	

@app.route('/testeDB', methods=['GET'])
def testeDB():	
	uri = "mongodb+srv://appbasicuser:appbasicusert3st3@cluster0-jvnpg.mongodb.net/test?retryWrites=true"
	client = pymongo.MongoClient(uri)
	db = client.test
	print(str(db))
	name = db.names
	dir(name)
	return (str(db))