#!/usr/bin/python3
"""
Queries the `Reddit API`, prints the titles of the first 10
hot posts listed for a given subreddit
"""

import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{subreddit}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}  # Set a custom User-Agent header
    response = requests.get(url, headers=headers)

    data = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print("None")
