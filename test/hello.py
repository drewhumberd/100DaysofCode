from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)
current_year = datetime.now().year

@app.route("/")
def hello():
    return render_template("index.html", year=current_year)

@app.route("/guess/<name>")
def guess(name):
    params = {"name": name}
    age_response = requests.get("https://api.agify.io", params=params).json()
    age = age_response["age"]
    gender_response = requests.get("https://api.genderize.io", params=params).json()
    gender = gender_response["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender, year=current_year)

@app.route("/blog")
def blog():
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=blog_response)

if __name__ == "__main__":
    app.run(debug=True)