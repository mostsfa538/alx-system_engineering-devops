#!/usr/bin/python3
""" How many subs """
import requests


def number_of_subscribers(subreddit):
    """
        that queries the Reddit API and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {'User-agent': 'Google Chrome Version 118.0.5993.120'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return (subs)
    else:
        return (0)
