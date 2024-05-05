from flask import Flask, render_template, url_for, request
import requests
from post import Post
import smtplib
import os

EMAIL = os.environ.get("EMAIL_ADDRESS")
APP_PASS = os.environ.get("GOOGLE_APP_PASS")

app = Flask(__name__)

posts = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()
post_objects = []
for post in posts:
    post_obj = Post(
        post_id=post["id"],
        title=post["title"],
        subtitle=post["subtitle"],
        body=post["body"],
        date=post["date"],
        author=post["author"]
        )
    post_objects.append(post_obj)

@app.route("/")
def hello():
    return render_template('index.html', posts=post_objects)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        headline = "Contact Me"
    elif request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=APP_PASS)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:New message!\n\nName: {data['name']}\nEmail: {data['email']}\
                \nPhone: {data['phone']}\nMessage: {data['message']}".encode("utf-8")
                )
        headline = "Successfully sent your message"
    return render_template('contact.html', headline=headline)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)