#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def alone_HBNB():
    return "HBNB!"

@app.route("/c/<text>", strict_slashes=False)
def C_and_text(text):
    return "C " + text.replace('_', ' ')

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def Python_and_text(text="is cool"):
    return "Python " + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
