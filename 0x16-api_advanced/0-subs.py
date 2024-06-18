#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "myCustomUserAgent/0.1"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        elif response.status_code == 301:  # Redirect
            return 0
        elif response.status_code == 404:  # Not found
            return 0
        else:
            return 0
        
    except requests.RequestException:
        return 0

