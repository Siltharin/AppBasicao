from flask import Flask, Response, request, render_template
from formCadastro import *


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
	

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/saveForm', methods=['POST'])
def saveForm():
	return saveCadastro()

@app.route('/listForm', methods=['POST'])
def listForm():	
	return listCadastro()


if __name__ == "__main__":
	app.run()
	