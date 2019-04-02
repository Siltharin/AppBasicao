import requests


def verifyFbToken(fbtoken, fbuserid):
    accesstokenurl = 'https://graph.facebook.com/' + fbuserid + '/access_token=' + fbtoken
    appToken = requests.get(accesstokenurl).json()