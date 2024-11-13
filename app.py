from flask import Flask, request, render_template, redirect, url_for
import blogpost_storage

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the index page displaying all listed blog posts
    :return: index template
    """
    blog_posts = blogpost_storage.read_blogposts()
    print(blog_posts)
    return render_template('index.html', post=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handles new blogposts
    :return: add.html
    """
    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("new_post")
        blogpost_storage.add_blogpost(title=title, author=author, content=content)
        return redirect(url_for("index"))
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """
    Handles deleting blogposts by passing the ID of the post
    :param post_id: id of blogpost to delete
    :return: index.html
    """
    blogpost_storage.delete_blogpost(id=post_id)
    return redirect(url_for("index"))


@app.route('/delete/<int:post_id>')
def delete_confirmation(post_id):
    """
    Handles the confirmation for deleting blogposts
    :param post_id:
    :return:
    """
    return render_template('delete.html', post_id=post_id)


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Handles updating existing blogposts
    :param post_id: the id of the blogpost
    :return: update.html
    """
    post = blogpost_storage.fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404
    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")
        blogpost_storage.update_blogpost(id=post_id, title=title, content=content)
        return redirect(url_for("index"))
    return render_template('update.html', post=post)


if __name__ == "__main__":
    """Runs the app on port 5001"""
    app.run(host="0.0.0.0", port=5001, debug=True)
