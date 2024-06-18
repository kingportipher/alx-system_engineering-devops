#!/usr/bin/python3

"""
Script that queries subscribers on Reddit subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyCoolScript/1.0"}  # Replace with your identifier

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

