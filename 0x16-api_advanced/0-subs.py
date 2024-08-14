#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "RedditSubscriberCounter/0.1 by Lawre"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError, KeyError):
        return 0  # Return 0 if there is any issue


if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    print(f"Number of subscribers: {number_of_subscribers(subreddit_name)}")
