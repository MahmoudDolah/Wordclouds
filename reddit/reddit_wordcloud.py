#! /usr/bin/env python3
"""Gets all of the comments written by a reddit user and outputs a word cloud of them"""

import matplotlib.pyplot as pylt
import praw
from wordcloud import WordCloud

def get_user(r):
    """Returns a user object"""
    username = input("Enter Reddit username: ")
    user = r.get_redditor(username)
    return user

def get_comments(user):
    """Returns all of the user's comments"""
    comments = ''
    for comment in user.get_comments(limit=None):
        comments = comments + ' ' + comment.body
    return comments
    
def make_wordcloud(comments):
    """Creates a word cloud based on the string input"""
    cloud = WordCloud().generate(comments)
    pylt.imshow(cloud)
    pylt.axis("off")
    pylt.show()
    
if __name__ == "__main__":
    r = praw.Reddit(user_agent="Get User and make wordcloud of comments")
    user = get_user(r)
    comments = get_comments(user)
    make_wordcloud(comments)
    