#!/usr/bin/python3
"""function that queries the Reddit API and
 returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ Return the total number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
