#!/usr/bin/python3
""" Top Ten """
import requests


def top_ten(subreddit):
    """
        prints the titles of the first
        10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = {'User-agent': 'Google Chrome Version 118.0.5993.120'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        top = [post['data']['title'] for post in data['data']['children']][:10]
        for i in top:
            print(i)
    else:
        print("None")
