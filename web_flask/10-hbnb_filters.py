#!/usr/bin/python3
from flask import Flask, render_template, abort
from models.state import State
from models.amenity import Amenity
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown_storage(something):
    """this function is called at the end to close storage"""
    storage.close()

@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    state_list = storage.all(State).values()
    amenity_list = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', state_list=state_list, amenity_list=amenity_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
