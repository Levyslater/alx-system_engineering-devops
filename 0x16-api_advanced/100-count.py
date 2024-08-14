#!/usr/bin/python3
"""Module for a function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """
    Write a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted count of
    given keywords (case-insensitive, delimited by spaces. Javascript should
    count as javascript, but java should not).
    """
    if word_dict is None:
        word_dict = {}

    if not word_dict:
        # Initialize the word dictionary with case-insensitive keys
        for word in word_list:
            word_lower = word.lower()
            if word_lower not in word_dict:
                word_dict[word_lower] = 0

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'reddit-word-counter'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after')

        for post in children:
            title = post['data']['title'].lower().split()
            for word in word_dict:
                word_dict[word] += title.count(word)

    except Exception:
        return None

    if after:
        count_words(subreddit, word_list, after, word_dict)
    else:
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f'{word}: {count}')


if __name__ == "__main__":
    count_words('python', ['Python', 'java', 'Javascript', 'programming'])
