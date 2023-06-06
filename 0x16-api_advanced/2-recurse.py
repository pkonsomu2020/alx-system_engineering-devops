#!/usr/bin/python3
"""
Returns a list of all topics for all hot articles
for a given Reddit subreddit
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Set a custom User-Agent header
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after:
            recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    else:
        return None
