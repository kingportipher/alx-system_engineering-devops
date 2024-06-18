#!/usr/bin/python3
"""
Recursive script to retrieve hot post titles from a given Reddit subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 100,
        "after": after
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            
            if not children:
                return hot_list if hot_list else None
            
            for child in children:
                hot_list.append(child.get("data", {}).get("title", ""))
            
            after = data.get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        
        elif response.status_code in [301, 404]:
            return None
        
        else:
            return None

    except requests.RequestException:
        return None

