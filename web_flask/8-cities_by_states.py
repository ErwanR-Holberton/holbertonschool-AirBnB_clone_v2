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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """print all cities in all states"""
    state_list = storage.all(State).values()
    return render_template("8-cities_by_states.html", all_states=state_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
