#!/usr/bin/python3
"""Count it"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Write a recursive function that queries the Reddit API,
        parses the title of all hot articles"""

    if not word_list or word_list == [] or not subreddit:
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data').get('children')

    for post in data:
        title = post.get('data').get('title').lower()
        for word in word_list:
            if word.lower() in title:
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + title.count(word)

    after = response.json().get('data').get('after')

    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_subs = sorted(word_count.items(),
                             key=lambda x: x[1], reverse=True)
        for sub in sorted_subs:
            if sub[1] != 0:
                print("{}: {}".format(sub[0], sub[1]))

        return word_count
