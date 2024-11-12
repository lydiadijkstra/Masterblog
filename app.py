from flask import Flask, request, render_template, redirect, url_for
import blogpost_storage

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = blogpost_storage.read_blogposts()
    print(blog_posts)
    return render_template('index.html', post=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("new_post")

        blogpost_storage.add_blogpost(title=title, author=author, content=content)

        return redirect(url_for("index"))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
