#! /usr/bin/env python3
"""A script which gets the last 200 tweets and outputs a word cloud of those tweets"""

import matplotlib.pyplot as pylt
from wordcloud import WordCloud
import tweepy
URL_WORDS = ["http", "https", "com/", "io/", "co", "amp", "rt"]


def authenticate():
    """Handles authentication with twitter API. Returns api object."""
    auth = tweepy.OAuthHandler("INSERT CONSUMER KEY","INSERT CONSUMER SECRET")
    auth.set_access_token("INSERT ACCESS TOKEN", "INSERT ACCESS TOKEN SECRET")
    api = tweepy.API(auth)
    return api

def get_all_tweets(api):
    """Gets last 200 tweets and returns them in a list"""
    user_handle = input("Enter twitter handle of user: ")
    all_tweets = api.user_timeline(screen_name=str(user_handle), count=200)
    return all_tweets

def parse_out_urls(all_tweets):
    """Parses out url related words/phrases like 'http', etc."""
    for tweet in all_tweets:
        for word in URL_WORDS:
            if word in tweet.text:
                tweet.text = tweet.text.replace(word, "")
    return all_tweets

def make_word_cloud(all_tweets):
    """Creates word cloud and outputs image"""
    tweets = ""
    for tweet in all_tweets:
        tweets = tweets + str(tweet.text) + " "
    cloud = WordCloud().generate(tweets)
    pylt.imshow(cloud)
    pylt.axis("off")
    pylt.show()

if __name__ == "__main__":
    api = authenticate()
    all_tweets = get_all_tweets(api)
    parsed_tweets = parse_out_urls(all_tweets)
    make_word_cloud(parsed_tweets)
    