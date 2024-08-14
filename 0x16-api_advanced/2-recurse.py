#!/usr/bin/python3
"""Contains the recurse function to get all hot post titles of a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Mozilla/10.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    data = response.json().get("data", {})
    after = data.get("after")
    count += data.get("dist", 0)

    children = data.get("children", [])
    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
