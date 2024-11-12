import json
from idlelib.autocomplete import FILES

JSON_FILE = "blogposts_data.json"


def read_blogposts():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            blog_posts = json.load(file)
            return blog_posts
    except FileNotFoundError as e:
        return []


def save_blogposts(blog_posts):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(blog_posts, file, indent=4)


def add_blogpost(author, title, content):
    blog_posts = read_blogposts()
    autoincrement_id = blog_posts[-1]["id"] +1 if blog_posts else 1

    new_blogpost = {
    "id": autoincrement_id,
    "author": author,
    "title": title,
    "content": content
    }

    blog_posts.append(new_blogpost)
    save_blogposts(blog_posts)


def update_blogpost(id, title, content):
    blog_posts = read_blogposts()
    for post in blog_posts:
        if post["id"] == id:
            if title:
                post["title"] == title
            if content:
                post["content"] == content
            break
    else:
        print("No blogpost was found with that ID {id}")
        return

    save_blogposts(blog_posts)


def delete_blogpost(id):
    blog_posts = read_blogposts()

    blog_posts = [post for post in blog_posts if post["id"] != id]

    save_blogposts(blog_posts)