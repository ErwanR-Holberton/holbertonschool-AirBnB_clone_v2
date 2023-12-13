#!/usr/bin/python3
"""flask app to return web pages depending on routes"""
from flask import Flask, render_template, abort
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(something):
    """this function is called at the end to close storage"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """print all states an cities or just those in the selected state"""
    state_list = storage.all(State).values()
    if id is None:
        return render_template("9-states.html", all_states=state_list, id=None)
    for state in state_list:
        if state.id == id:
            return render_template("9-states.html", state=state, id=id)
    abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
