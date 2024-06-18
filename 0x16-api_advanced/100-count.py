#!/usr/bin/python3
"""
Recursive script to count keyword occurrences in hot post titles of a given Reddit subreddit.
"""

import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """Count keywords in hot articles titles recursively and print the sorted count."""
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
            
            if not children and not after:
                print_sorted_word_count(word_count)
                return

            for child in children:
                title = child.get("data", {}).get("title", "").lower()
                words = title.split()
                for word in words:
                    cleaned_word = ''.join(filter(str.isalpha, word))
                    if cleaned_word in word_list:
                        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
            
            after = data.get("after")
            if after:
                count_words(subreddit, word_list, after, word_count)
            else:
                print_sorted_word_count(word_count)
        
        elif response.status_code in [301, 404]:
            print_sorted_word_count(word_count)
            return

        else:
            print_sorted_word_count(word_count)
            return

    except requests.RequestException:
        print_sorted_word_count(word_count)
        return

def print_sorted_word_count(word_count):
    """Print the word count dictionary sorted by count and alphabetically."""
    sorted_word_count = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")

def recurse(subreddit, word_list):
    """Wrapper function to initiate the recursive counting process."""
    word_list_lower = [word.lower() for word in word_list]
    count_words(subreddit, word_list_lower)


