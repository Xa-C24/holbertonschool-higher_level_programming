#!/usr/bin/python3
"""Import requests and csv module"""


import requests
import csv


def fetch_and_print_posts():
    """Function for retrieving and displaying post titles"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Function for retrieving and saving posts in a CSV file"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = [{'id': post['id'], 'title': post['title'],
                  'body': post['body']} for post in response.json()]

        with open("open.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
