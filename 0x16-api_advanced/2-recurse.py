#!/usr/bin/python3
""" Recurse it """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
        returns a list containing the titles
        of all hot articles for a given subreddit
    """
    global after
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = {'User-agent': 'Google Chrome Version 118.0.5993.120'}
    params = {'after': after}
    response = requests.get(url, headers=user_agent, allow_redirects=False,
                            params=params)

    if response.status_code == 200:
        data = response.json()
        after_code = data['data']['after']
        if after_code:
            after = after_code
            recurse(subreddit, hot_list)
        top = [post['data']['title'] for post in data['data']['children']]
        for i in top:
            hot_list.append(i)
        return (hot_list)
    else:
        return (None)
