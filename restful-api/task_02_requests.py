#!/usr/bin/python3
"""
Task 2: Consuming and processing data from an API using Python
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder API
    and print the status code and titles of the posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder API
    and save selected fields (id, title, body)
    into a CSV file called posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(structured_posts)
