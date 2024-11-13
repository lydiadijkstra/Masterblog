# Masterblog

Masterblog is a basic Flask application for managing blog posts. This app allows users to create, read, update, and delete (CRUD) blog posts, with data stored in a JSON file.

Features
View all blog posts: See a list of all posts on the homepage.
Add a new blog post: Create a new post with a title, author, and content.
Edit a blog post: Update the title and content of an existing post.
Delete a blog post: Remove a post after confirming deletion.

Installation:
1. Clone the repository
2. Create a virtual environment
3. Install dependencies

Routes
/: View all blog posts.
/add: Add a new blog post.
/update/<post_id>: Update an existing blog post.
/delete/<post_id>: Delete a blog post (with confirmation).

File Structure
app.py: Main Flask application file with route definitions.
blogpost_storage.py: Module for handling blog post data storage and retrieval.
templates/: Folder containing HTML templates for different pages (index, add, update, delete).
static/: Folder containing CSS files for styling.

