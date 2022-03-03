from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

r = requests.get("https://api.npoint.io/b489d224d165c19fff02")
data = r.json()
posts_objects = []
for post in data:
    posts_objects.append(Post(post['id'], post['title'], post['subtitle'], post['body']))


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts_objects)


@app.route('/post/<blog_id>')
def get_body(blog_id):
    return render_template("post.html", post_id=blog_id, all_posts=posts_objects)


if __name__ == "__main__":
    app.run(debug=True)
