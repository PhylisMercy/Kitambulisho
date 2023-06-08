#!/usr/bin/python3
""" Starts a Flash Web Application """
import os
import uuid

from models import storage
from models.city import City
from models.Collection_Stations import Kitambulisho_Collection_Station
from models.collector_signoff import Kitambulisho_Collection_Station_SignOff
from models.Counties import County
from models.Kitambulisho_Collection_Register import Kitambulisho_Collection_Register
from models.remuneration import Remuneration
from models.review import Review
from models.user import User
from models.vitambulisho import Kitambulisho
from os import environ
from flask import Flask, render_template

app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    if STORAGE_TYPE == "db":
        states = storage.all('County').values()
        amenities = storage.all("Kitambulisho").values()
        places = storage.all("Kitambulisho_Collection_Station").values()
    else:
        states = storage.all(County).values()
        amenities = storage.all(Kitambulisho).values()
        places = storage.all(Kitambulisho_Collection_Station).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = sorted(amenities, key=lambda k: k.name)

    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
