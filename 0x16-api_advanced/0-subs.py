#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """function to get number of subscribers in reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    data = requests.get(url)

    if data.json().get("data").get("subscribers"):
        return data.json().get("data").get("subscribers")
    else:
        return 0
