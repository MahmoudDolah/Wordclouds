#! /usr/bin/env python3

import matplotlib.pyplot as pylt
from wordcloud import WordCloud
import tweepy
import auth_keys

def authenticate():
    auth = tweepy.OAuthHandler(auth_keys.consumer_key, auth_keys.consumer_secret)
    auth.set_access_token(auth_keys.access_token, auth_keys.access_token_secret)
    api = tweepy.API(auth)
    return api

def get_all_tweets(api):
    user_handle = input("Enter twitter handle of user: ")
#    user = api.get_user(user_handle)
#    print("User: " + str(user))
    all_tweets = api.user_timeline(screen_name=str(user_handle), count=4)
    return all_tweets

def make_wordcloud(all_tweets):
    tweets = ""
    for tweet in all_tweets:
        tweets = tweets + str(tweet.text) + " "
    cloud = WordCloud().generate(tweets)
    pylt.imshow(cloud)
    pylt.axis("off")
    pylt.show()

def main():
    api = authenticate()
    all_tweets = get_all_tweets(api)
#    print(all_tweets)
    make_wordcloud(all_tweets)

if __name__ == "__main__":
    main()
    