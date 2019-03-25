from flask import Flask, Response, request, render_template


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def main():
	return render_template('index.html')