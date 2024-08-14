#!/usr/bin/python3
"""
Module that contains the function top_ten
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    Prints the titles of the top ten hot posts for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    headers = {'User-Agent': 'RedditTopTen/0.1 by Levyslater'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(None)
        return

    try:
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get('data', {}).get('title', None))
    except (KeyError, TypeError):
        print(None)


if __name__ == "__main__":
    # test the code functionality
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Please provide a subreddit name.")
