from flask import Flask, render_template
import blogpost_storage

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = blogpost_storage.read_blogposts()
    print(blog_posts)
    return render_template('index.html', post=blog_posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
