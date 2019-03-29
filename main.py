from flask import Flask, Response, request, render_template
from formCadastro import *
import datetime


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
	

@app.route('/')
def main():
	return render_template('index.html')


@app.route('/saveForm', methods=['POST'])
def saveForm():
	token = request.args.get("token")
	item = {"contact": request.args.get("contact"), 
			"message": request.args.get("message"),
			"timestamp": datetime.datetime.utcnow()}
	return saveCadastro(item)

@app.route('/listForm', methods=['POST'])
def listForm():	
	return listCadastro()


if __name__ == "__main__":
	app.run()
	