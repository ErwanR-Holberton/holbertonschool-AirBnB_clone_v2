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
    """route / returns this"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
