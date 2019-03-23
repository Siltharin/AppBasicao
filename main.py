from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
	
    
@app.route('/testeDB', methods=['GET'])
def testeDB():
	uri = 'mongodb://heroku_39k79224:usert3st3@ds121406.mlab.com:21406/heroku_39k79224'
	client = MongoClient(uri)
	db = client['heroku_39k79224']
	name = db.names
	dir(name)
	collection = db.collection_names(include_system_collections=False)
	for collect in collection:
    	print collect
	print(db.names.find_one())
	#help(name)  
	#print (str(name))
	
	SEED_DATA = [
		{'decade': '1970s','artist': 'Debby Boone','song': 'You Light Up My Life','weeksAtOne': 10},
		{'decade': '1980s','artist': 'Olivia Newton-John','song': 'Physical','weeksAtOne': 10},
		{'decade': '1990s','artist': 'Mariah Carey','song': 'One Sweet Day','weeksAtOne': 16}
	]
	
	songs = db['songs']
	#songs.insert_many(SEED_DATA)
	#query = {'song': 'One Sweet Day'}
	#songs.update(query, {'$set': {'artist': 'Mariah Carey ft. Boyz II Men'}})
	#cursor = songs.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)
	#for doc in cursor:
	#	print ('In the %s, %s by %s topped the charts for %d straight weeks.' %
	#		(doc['decade'], doc['song'], doc['artist'], doc['weeksAtOne']))
	#    db.drop_collection('songs')
	#   client.close
	return (SEED_DATA)
	

@app.route('/')
def main():
	#testeDB()
	return render_template('index.html')
 	


	
	
	
