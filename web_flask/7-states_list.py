#!/usr/bin/python3
"""flask app to return web pages depending on routes"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(something):
    """this function is called at the end to close storage"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """print all states in storage"""
    state_list = storage.all(State)
    return render_template("7-states_list.html", all_states=state_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
