from flask import Flask, Response, request, redirect
from formCadastro import *
from authentication import *
import datetime


app = Flask(__name__)

@app.route('/')
def main():
	return redirect('static/index.html')


@app.route('/listForm', methods=['POST'])
def listForm():	
	authenticate()
	return listCadastro()

@app.route('/saveForm', methods=['POST'])
def saveForm():
	authenticate()
	item = {"contact": request.args.get("contact"), 
			"message": request.args.get("message"),
			"timestamp": datetime.datetime.utcnow()}
	return saveCadastro(item)


def authenticate():
	fbtoken = request.args.get("fbtoken")
	if fbtoken != '':
		fbuserid = request.args.get("fbuserid")
		verifyFbToken(fbtoken, fbuserid)
	elif gltoken != '':
		verifyGlToken(gltoken)



if __name__ == "__main__":
	app.run(debug=True)
	