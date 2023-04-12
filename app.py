from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/about")
@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact")
@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/users")
@app.route("/reqres-data.html")
def users():
    return render_template('reqres-data.html')

@app.route("/mobiles")
@app.route("/mobiles.html")
def mobiles():
    return render_template('mobiles.html')

from postdata import posts

@app.route("/post/int:post_id>")
def post(post_id):
    post = posts[post_id]
    return render_template('post.html', title = post['title'], p = post)

from json import dumps

@app.route("/json_posts")
def json_posts():
    data = {
        'data': posts,
        'total': len(posts)
    }
    return dumps(data)

@app.errorhandler(404)
def err_404(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)