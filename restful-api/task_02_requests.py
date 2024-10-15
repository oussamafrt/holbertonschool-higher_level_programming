#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch the posts")

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            structure_data = [{"id": post["id"], "title": post["title"], "body": post["body"]}]

        with open("posts.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structure_data)
        print("Posts saved to post.csv")
    else:
        print("Failed to fetch posts")
