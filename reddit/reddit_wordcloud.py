#! /usr/bin/env python3

import matplotlib.pyplot as pylt
import praw
from wordcloud import WordCloud

def get_user(r):
    username = input("Enter Reddit username: ")
    user = r.get_redditor(username)
    return user

def get_comments(user):
    comments = '' 
    for c in user.get_comments(limit=None):
        comments = comments + ' ' + c.body
    return comments
    
def make_wordcloud(comments):
    cloud = WordCloud().generate(comments)
    pylt.imshow(cloud)
    pylt.axis("off")
    pylt.show()
    
def main():
    r = praw.Reddit(user_agent="Get User and make wordcloud of comments")
    user = get_user(r)
    comments = get_comments(user)
    make_wordcloud(comments)
    
if __name__ == "__main__":
    main()