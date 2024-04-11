#!/usr/bin/python3
"""module to return top ten in reddit"""

import requests


def top_ten(subreddit):
    """function that print the titles and top10"""
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)

    data = requests.get(url, params={"limit": 10})

    if data.status_code != 200:
        print(None)
        return

    posts = data.json().get("data").get("children")

    if posts:
        for post in posts:
            print(post.get("data").get("title"))
    else:
        print(None)
