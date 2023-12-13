#!/usr/bin/python3
"""flask app to return web pages depending on routes"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """route / returns this"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def alone_HBNB():
    """route /hbnb returns this"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_and_text(text):
    """route /c/some text returns C + the text"""
    return "C " + text.replace('_', ' ')


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def Python_and_text(text="is cool"):
    """web page with Python +text with a default value"""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """print the number"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
