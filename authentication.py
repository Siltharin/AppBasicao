import requests


def verifyFbToken(fbtoken, fbuserid):
    accesstokenurl = 'https://graph.facebook.com/' + fbuserid + '/access_token=' + fbtoken
    appToken = requests.get(accesstokenurl).json()
    

    
#	clientId = xxxxxxxxxxxx
#	clientSecret = xxxxxxxxxxxxx
#	accesstokenurl = 'https://graph.facebook.com/oauth/access_token?client_id=' 
#					+ clientId + '&client_secret=' 
#					+ clientSecret + '&grant_type=client_credentials'
#	appToken = requests.get(accesstokenurl).json()['access_token']
#	debugtokenurl = 'https://graph.facebook.com/debug_token?input_token=' 
#						+ userToken + '&access_token=' + appToken
#	try:
#	    userId = requests.get(debugtokenurl).json()['data']['user_id']
#	except (ValueError, KeyError, TypeError) as error:
#	    return error
#	return userId
#https://graph.accountkit.com/v1.1/access_token?grant_type=authorization_code&code=xxxxxxxxxx&access_token=AA|yyyyyyyyyy|zzzzzzzzzz
