#!/usr/bin/python3
"""Recursive function"""

import requests

def recurse(subreddit, hot_list=[], after=''):
    """Recursive function that queries Reddit API and returns a list"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    data = requests.get(url, headers=headers, params={"limit": 100, "after":after})

    if data.status_code != 200:
        return None
    
    posts = data.json().get("data").get("children")

    if posts:
        for post in posts:
            hot_list.append(post.get("data").get("title"))
            after = data.json().get("data").get("after")
            if after:
                return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
