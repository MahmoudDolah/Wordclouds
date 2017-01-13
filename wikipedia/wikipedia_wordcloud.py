#! /usr/bin/env python3
"""A script that gets a wikipedia article and makes a word cloud of the text in it"""
import random
import itertools
import wikipedia
import matplotlib.pyplot as pylt
from wordcloud import WordCloud

def search_wikipedia():
    """Searches Wikipedia for term specified by user and returns a page object"""
    lookup = input("Enter search item: ")
    if lookup == '':
        rand_num = random.randrange(14)
        with open('test.txt') as f:
            for i in itertools.islice(f, 0, rand_num):
                pass
            lookup = f.readline()
    page = wikipedia.page(lookup)
    print("Searching for " + page.title)
    return page

def make_cloud(text):
    """Makes word cloud. Takes in a string."""
    cloud = WordCloud().generate(text)
    pylt.imshow(cloud)
    pylt.axis("off")
    pylt.show()

if __name__ == "__main__":
    page = search_wikipedia()
    make_cloud(page.summary)
    