from requests_oauthlib import OAuth1Session
from twlib.error import *
import json

class TwitterSession:
    def __init__(self, oauth_keys):
        self.oauth1session = OAuth1Session(
            oauth_keys["consumer_key"],
            oauth_keys["consumer_secret"],
            oauth_keys["access_token"],
            oauth_keys["access_token_secret"]
        )

    def post(self, api_name, params):
        url = 'https://api.twitter.com/1.1/' + str(api_name) + '.json'
        req = self.oauth1session.post(url, params)
        if req.status_code != 200:
            raise TwitterRequestError(req.status_code)

    def tweet(self, sentence):
        api_name = "statuses/update"
        params = {"status" : str(sentence)}
        return self.post(api_name, params)

    def get(self, api_name, params):
        url = 'https://api.twitter.com/1.1/' + str(api_name) + '.json'
        req = self.oauth1session.get(url,params=params)
        if req.status_code != 200:
            raise TwitterRequestError(req.status_code)
        return req

    def get_hometimeline(self, count = 10):
        api_name= 'statuses/home_timeline'
        params = {'count' : count}
        return self.get(api_name, params)
