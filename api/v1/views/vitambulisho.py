#!/usr/bin/python3
# noinspection PyInterpreter,PyInterpreter
"""
This is a module that implements a blueprint
this blueprint is a kind of modularization of
flask applications.
The only requirement is that you will then
import this package file in main then register the
blueprint (app_views) as shown below

app.register_blueprint(app_views)

You can also override its url_prefix like so
app.register_blueprint(app_views, url_prefix="/diff/url")
"""
import os

from flask import jsonify, escape, abort, request, make_response

from api.v1.views import app_views
from models import storage, \
    City, County, Kitambulisho

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


@app_views.route('/amenities', strict_slashes=False)
def get_amenities():
    """ Function returns list of amenities in json format
    """
    temp = list()

    if True:
        if STORAGE_TYPE == "db":
            amenities = storage.all('Kitambulisho').values()
        else:
            amenities = storage.all(Kitambulisho).values()
            dummy = list()

            for value in amenities:
                dummy.append(value)
            amenities = dummy

        for val in amenities:
            temp.append(val.to_dict())
        if len(temp) < 1:
            abort(404)
        else:
            return jsonify(temp)


@app_views.route('/amenities/<amenity_id>', strict_slashes=False)
def get_amenity(amenity_id):
    """ Function returns list of cities by states and
    displays/renders them in a html document.
    when no get parameter is provided it will list all available
    states.
    When a state_id is provided it will list all cities within than state
    When a non_existent state_id is provided (url/states/<invalid_state_id>
    the page displays "Not found!"
    """

    if STORAGE_TYPE == "db":
        # amenities = storage.all("Kitambulisho").values()
        amenities = storage.get("Kitambulisho", amenity_id)
        if not amenities:
            abort(404)
    else:
        amenities = storage.get(Kitambulisho, amenity_id)
    return jsonify(amenities.to_dict())


@app_views.route('/amenities/<amenity_id>/places', strict_slashes=False)
def get_place_of_amenity(amenity_id):
    """
    returns all places in which the particular ID number has been stored.
    curl localhost:5001/api/v1/amenities/<amenity_id>/places

    """
    if STORAGE_TYPE == "db":
        amenity = storage.get('Kitambulisho', amenity_id)
        if not amenity:
            abort(404)
        places = [place.to_dict() for place in amenity.collection_stations]
    else:
        amenity = storage.get(Kitambulisho, amenity_id)
        if not amenity:
            abort(404)
        places = [storage.get(Kitambulisho, amenity_id).to_dict()
                  for place_id in amenity.amenity_ids]
    return jsonify(places)


@app_views.route('/amenities/<amenity_id>/signoffs', strict_slashes=False)
def get_signoff_of_amenity(amenity_id):
    """
    returns all signoff forms in which the particular Amenity id  has been stored.
    curl localhost:5001/api/v1/amenities/<amenity_id>/signoffs

    """
    if STORAGE_TYPE == "db":
        amenity = storage.get('Kitambulisho', amenity_id)
        if not amenity:
            abort(404)
        places = [place.to_dict() for place in amenity.collection_registers]
    else:
        amenity = storage.get(Kitambulisho, amenity_id)
        if not amenity:
            abort(404)
        places = [storage.get(Kitambulisho, amenity_id).to_dict()
                  for place_id in amenity.amenity_ids]
    return jsonify(places)


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False,
                 methods=['DELETE'])
def del_amenity(amenity_id):
    """ Function returns list of cities by states and
    displays/renders them in a html document.
    when no get parameter is provided it will list all available
    states.
    When a state_id is provided it will list all cities within than state
    When a non_existent state_id is provided (url/states/<invalid_state_id>
    the page displays "Not found!"
    """
    if amenity_id:
        if STORAGE_TYPE == "db":
            del_obj = storage.get("Kitambulisho", escape(amenity_id))
        else:
            # Handles File Storage
            # storage.get return an object dictionary else None
            del_obj = storage.get(Kitambulisho, escape(amenity_id))
        if del_obj:
            # storage.delete returns true on success else false
            del_status = storage.delete(del_obj)
            if del_status:
                return jsonify({})
            else:
                abort(404)
        else:
            abort(404)


@app_views.route('/amenities',
                 strict_slashes=False, methods=['POST'])
def post_amenities():
    """ Creates a new State and initializes it with a state name
    if requested dictionary is none output 'Not a JSON'
    if post data does not contain the key 'name' output 'Missing name'
    On success return a status of 201 else 400
    curl -X POST http://0.0.0.0:5000/api/v1/places/2ec62c4b-f8ea-4a52-b68d-9b06eb7fb927/amenities/ -H "Content-Type: application/json" -d '{"name": "bujumbura", "user_id": "2655e743-ff9e-4837-ac09-1dadf9f7ea26"}'
    curl -X POST http://0.0.0.0:5001/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "Libianca", "ID_Number": "9865552"}'

    """

    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    if req_json.get("name") is None:
        abort(400, 'Missing name')
    if req_json.get("ID_Number") is None:
        abort(400, 'Missing ID_Number')
    new_object = Kitambulisho(**req_json)
    new_object.save()
    if STORAGE_TYPE == "db":
        amenity_obj = storage.get("Kitambulisho", escape(new_object.id))
    else:
        # Handles File Storage
        # storage.get return an object dictionary else None
        amenity_obj = storage.get(Kitambulisho, escape(new_object.id))

    return make_response(jsonify(amenity_obj.to_dict()), 201)
    # return jsonify(new_object.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False, methods=['PUT'])
def update_amenity(amenity_id):
    """ Updates a city's values
    if requested dictionary is none output 'Not a JSON'
    if post data does not contain the key 'name' output 'Missing name'
    On success return a status of 201 else 400
    curl -X POST http://0.0.0.0:5001/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "Libianca", "ID_Number": "9865552"}'

    """
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    if req_json.get("name") is None:
        abort(400, 'Missing name')
    status = storage.update(Kitambulisho, amenity_id, req_json)

    if status:
        return jsonify(status.to_dict())
    else:
        abort(404)
