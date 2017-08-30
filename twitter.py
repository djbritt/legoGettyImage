import random
from random import randint
import flask
from flask import render_template
import os
import random
# from urllib2 import Request, urlopen, URLError
import json
from pprint import pprint
# from pygments import highlight, lexers, formatters
import requests_oauthlib, requests
app = flask.Flask(__name__)

i = 0
url = "https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&count=11"
oauth = requests_oauthlib.OAuth1(
    "3PAcYrddewZ3uWXyLFvs7A29l", 
    "w1EmN1J53pHGzIV6SPEvVaefD33m1H9jPEkbEObGbB5KWhGER5",
    "2298684023-f0UjDI1inFCpEo3Snx0ia664DlN7noNxJ6UuDyX",
    "J3fNjNpmTr4YVNFHYvuGfVWRmRlGi8PiSPUV3NJWnatBD"
)

r = requests.get(url, auth=oauth)
# response = requests.get(url, auth=oauth)
# t = response.json()
t = r.json()

@app.route('/') 
def index():
    global r
    global i
    global t
    # t = r.text
    # tweets = r.text
    # tweets = t["statuses"]
    last = len(t["statuses"])
    
    tweets = t["statuses"][i-1]["text"]
    urlId = t["statuses"][i-1]["id"]
    # twitterUser = t["statuses"][i-1]["entities"]["user_mentions"][0]["screen_name"]
    twitterUser = "t"
    # tweets = len(t["statuses"][i]["text"])
    if i >= last:
        i=0
    i+=1
    i = r.text
    # tweets = i
    # return t
    
    # tweets = len(t["statuses"][i]["text"])
    
    return render_template('index1.html', tweetCount=tweets, i=i, tId=urlId, tUser=twitterUser)
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)