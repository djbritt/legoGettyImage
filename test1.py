from flask import Flask
import os
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return "hello world"
    oauthkeys = open("../oauthkeys.txt", "rb").read()
    return oauthkeys
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)