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

from flask import request
from flask_mail import Mail, Message

# Set up email server configurations
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your-email@gmail.com' # insert your gmail 
app.config['MAIL_PASSWORD'] = 'your-email-password' # insert your password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Create a Flask route for the contact page
@app.route("/contact.html", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve the submitted form data for name, email, and message
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Create and send the email message
        msg = Message('New contact submission', sender='your-email@gmail.com', 
                      recipients=['recipient-email@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)
        return render_template('contact.html', sent=True)
    else:
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

@app.route("/post/<int:post_id>")
def single_post(post_id):
    post = posts[post_id - 1]  # Retrieve the post from the 'posts' list based on the URL
    return render_template('single-post.html', post=post)

@app.route("/post")
def all_post():
    return render_template('all-post.html', posts=posts)

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