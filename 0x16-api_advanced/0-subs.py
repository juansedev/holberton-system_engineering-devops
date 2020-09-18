#!/usr/bin/python3
"""
   Write a function that queries the Reddit API and returns the number of
   subscribers (not active users, total subscribers) for a given subreddit.
   f an invalid subreddit is given, the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    """ Get a number of suscribers"""
    url = ('https://www.reddit.com/r/{}/about.json'.format(subreddit))
    head = {"User-Agent": "Mozilla/5.0"}
    j_response = requests.get(url, headers=head).json()
    if j_response.get('error') == 404:
        return 0
    return j_response.get('data').get('subscribers')
