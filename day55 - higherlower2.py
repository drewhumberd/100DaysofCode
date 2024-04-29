import random
from flask import Flask

app = Flask(__name__)

# def make_bold(function):
#     def wrapper():
#         return f"<b>{function()}</b>"
#     return wrapper

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/bye")
# @make_bold
# def bye():
    # return "Bye"

secret_number = random.randint(0,9)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9!</h1> \
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > secret_number:
        return "<h1 style='color: purple'>Too high, try again!</h1> \
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    elif guess < secret_number:
        return "<h1 style='color: red'>Too low, try again!</h1> \
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    else:
        return "<h1 style='color: green'>You found me!</h1> \
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)