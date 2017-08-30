import random
from random import randint
import flask
from flask import render_template
import os
# from urllib2 import Request, urlopen, URLError
import json
# from pygments import highlight, lexers, formatters
import requests_oauthlib, requests

app = flask.Flask(__name__)
i = 0
j = 25  
responseList = []
tweetList = []

url = "https://api.twitter.com/1.1/search/tweets.json?q=%23lego&count=11"
oauth = requests_oauthlib.OAuth1(
    os.getenv("oauth1"), 
    os.getenv("oauth2"),
    os.getenv("oauth3"),
    os.getenv("oauth4")
)

response = requests.get(url, auth=oauth)
t = response.json()

@app.route('/') 
def index():
    global i
    global t
    last = len(t["statuses"])
    if i >= last:
        i=0
    tweets = t["statuses"][i-1]["text"]
    urlId = t["statuses"][i-1]["id"]
    twitterUrl = "https://www.twitter.com/statuses/"
    twitterUser = t["statuses"][i-1]["user"]["screen_name"]
    currentI = i
    i+=1
    
    global j
    if j >= 25:
        j=0
    if j==5:
        j+=1
    # j = randint(0,399)
    url = 'https://api.gettyimages.com:443/v3/search/images?fields=comp&phrase=legos&sort_order=most_popular'
    headers = {
        "Api-Key": os.getenv("gettyKey")
    }
    r = requests.get(url, headers=headers)
    # a = r.json()
    # return json.dumps(a, indent=2)
    gettyLength = len(r.json()["images"])
    a = r.json()["images"][j]["display_sizes"][0]["uri"]
    j += 1
    return render_template('index.html', getty=a, tweets=tweets, twitterLength=last, urlId=urlId, twitterUrl=twitterUrl, gettyCurrent=j, gettyLength=gettyLength, twitterUser=twitterUser, i=i)
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)