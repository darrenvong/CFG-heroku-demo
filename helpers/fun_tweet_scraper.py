# -*- coding: utf-8 -*-
from random import randrange
from bs4 import BeautifulSoup
import requests

AGENT_NAME = "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0"
HEADERS = {"User-Agent": AGENT_NAME}

def query_builder():
    funny_tweet_periods = ["since:2011-12-01 until:2011-12-31", "since:2012-03-01 until:2012-04-01",
                           "since:2013-07-31 until:2013-08-31"]
    return "from:paulienuh " + funny_tweet_periods[randrange(3)]

def get_funny_tweets(url, params={}, headers={}):
    """Retrieves a list of funny tweets in the following format:
    {"tweet": "...", "time": "...", "images": ["...", "..."]} (images list may be empty)
    """
    my_funny_req = requests.get(url, params=params, headers=headers)
    parser = BeautifulSoup(my_funny_req.text, "html.parser")
    full_tweets = parser.select(".tweet .content")

    # super compact way of returning a list of dictionaries using a construct known
    # as list comprehension
    return [{
                "text": tweet.select_one(".tweet-text").get_text(),
                "time": tweet.select_one("._timestamp").get_text(),
                "images": [image["src"] for image in tweet.select(".AdaptiveMedia img")]
            }
            for tweet in full_tweets]

if __name__ == '__main__':
    params = {"q" : "from:paulienuh since:2011-12-01 until:2011-12-31"}
    tweet_objs = get_funny_tweets("https://twitter.com/search", params=params, headers=HEADERS)
    print(tweet_objs)
