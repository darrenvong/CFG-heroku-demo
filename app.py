# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from helpers.fun_tweet_scraper import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.htm.j2")

@app.route('/latest_pauline_tweets')
def latest_tweets():
    search_url = "https://twitter.com/search"
    params = {"q" : query_builder()}

if __name__ == '__main__':
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True, port=80)
