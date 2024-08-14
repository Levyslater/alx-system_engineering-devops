#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "RedditSubscriberCounter/0.1 by Lawre"
    }
    try:
        # ensure you are not following redirects by setting value to false
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Raises HTTPError for bad responses (4xx, 5xx)
        response.raise_for_status()
        return 0  # If the subreddit doesn't exist or request fails, return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

    try:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
    except (ValueError, KeyError):
        return 0  # Return 0 if there's an issue with the JSON parsing

    return subscribers
