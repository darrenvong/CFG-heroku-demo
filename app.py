# -*- coding: utf-8 -*-
import os
import re
from dotenv import load_dotenv
from flask import Flask, render_template
from helpers.fun_tweet_scraper import query_builder, get_funny_tweets, HEADERS

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", title="CF:G Sheffield Ambassador Appreciation App")

@app.route('/latest_pauline_tweets')
def latest_tweets():
    search_url = "https://twitter.com/search"
    params = {"q" : query_builder()}
    tweet_objs = get_funny_tweets(search_url, params=params, headers=HEADERS)

    date_matcher = re.compile("\d+-\d+-\d+")
    start_date, end_date = date_matcher.findall(params["q"])

    return render_template("display_tweets.html", tweets=tweet_objs,
                            start=start_date, end=end_date,
                            title=f"Tweets by @paulienuh... from {start_date} to {end_date}")

if __name__ == '__main__':
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True)
