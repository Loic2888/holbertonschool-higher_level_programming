import requests
import csv

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print the status code
    and titles of all posts.
    """
    response = requests.get(BASE_URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts(csv_filename="posts.csv"):
    """
    Fetch all posts from JSONPlaceholder and save id, title, and body
    into a CSV file.
    """
    response = requests.get(BASE_URL)

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        data = []
        for post in posts:
            data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
        fieldnames = ["id", "title", "body"]
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Posts saved to {csv_filename}")
    else:
        print("Failed to fetch posts.")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
