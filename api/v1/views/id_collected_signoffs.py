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
    City, County, Kitambulisho, Kitambulisho_Collection_Station_SignOff

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


@app_views.route('/signoffs', strict_slashes=False)
def get_signoffs():
    """ Function returns list of amenities in json format
    """
    temp = list()

    if True:
        if STORAGE_TYPE == "db":
            amenities = storage.all('Kitambulisho_Collection_Station_SignOff').values()
        else:
            amenities = storage.all(Kitambulisho_Collection_Station_SignOff).values()
            dummy = list()

            for value in amenities:
                dummy.append(value)
            amenities = dummy

        for val in amenities:
            temp.append(val.to_dict())
        # if len(temp) < 1:
        #     abort(404)
        # else:
        return jsonify(temp)


@app_views.route('/signoffs/<signoff_id>', strict_slashes=False)
def get_signoff(signoff_id):
    """ Function returns list of cities by states and
    displays/renders them in a html document.
    when no get parameter is provided it will list all available
    states.
    When a state_id is provided it will list all cities within than state
    When a non_existent state_id is provided (url/states/<invalid_state_id>
    the page displays "Not found!"
    """
    if STORAGE_TYPE == "db":
        signoffs = storage.get("Kitambulisho_Collection_Station_SignOff", signoff_id)
        if not signoffs:
            abort(404)
    else:
        signoffs = storage.get(Kitambulisho_Collection_Station_SignOff, signoff_id)
    return jsonify(signoffs.to_dict())


@app_views.route('/signoffs/<signoff_id>',
                 strict_slashes=False,
                 methods=['DELETE'])
def del_signoff(signoff_id):
    """ Function returns list of cities by states and
    displays/renders them in a html document.
    when no get parameter is provided it will list all available
    states.
    When a state_id is provided it will list all cities within than state
    When a non_existent state_id is provided (url/states/<invalid_state_id>
    the page displays "Not found!"
    """
    if signoff_id:
        if STORAGE_TYPE == "db":
            del_obj = storage.get("Kitambulisho_Collection_Station_SignOff", escape(signoff_id))
        else:
            # Handles File Storage
            # storage.get return an object dictionary else None
            del_obj = storage.get(Kitambulisho_Collection_Station_SignOff, escape(signoff_id))
        if del_obj:
            # storage.delete returns true on success else false
            del_status = storage.delete(del_obj)
            if del_status:
                return jsonify({})
            else:
                abort(404)
        else:
            abort(404)


@app_views.route('/signoffs',
                 strict_slashes=False, methods=['POST'])
def post_signoff():
    """ Creates a signoff form in which claimant of lost kitambulisho is officializing collection of their PII.
    curl -X POST http://0.0.0.0:5001/api/v1/signoffs -H "Content-Type: application/json" -d '{"ID_Collector_Register_id": "1c6e9030-8e32-4334-8324-0dc5b516323a"}'
    """

    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    claims_register_id = req_json.get("ID_Collector_Register_id")
    if claims_register_id is None:
        abort(400, 'Missing ID_Collector_Register_id')

    # if req_json.get("ID_Number") is None:
    #     abort(400, 'Missing ID_Number')
    claims_register_object = storage.get("Kitambulisho_Collection_Register", escape(claims_register_id))
    if not claims_register_object:
        abort(404)

    new_object = Kitambulisho_Collection_Station_SignOff(**req_json)
    new_object.save()
    if STORAGE_TYPE == "db":
        signoff_obj = storage.get("Kitambulisho_Collection_Station_SignOff", escape(new_object.id))
    else:
        # Handles File Storage
        # storage.get return an object dictionary else None
        signoff_obj = storage.get(Kitambulisho_Collection_Station_SignOff, escape(new_object.id))

    return make_response(jsonify(signoff_obj.to_dict()), 201)
    # return jsonify(new_object.to_dict()), 201


@app_views.route('/signoffs/<signoff_id>',
                 strict_slashes=False, methods=['PUT'])
def update_signoff(signoff_id):
    """ Updates a city's values
    if requested dictionary is none output 'Not a JSON'
    if post data does not contain the key 'name' output 'Missing name'
    On success return a status of 201 else 400
    curl -X POST http://0.0.0.0:5001/api/v1/signoffs/<signoff_id> -H "Content-Type: application/json" -d '{"name": "Libianca", "ID_Number": "9865552"}'

    """
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    if req_json.get("status") is None:
        abort(400, 'Missing status')
    status = storage.update(Kitambulisho_Collection_Station_SignOff, signoff_id, req_json)

    if status:
        return jsonify(status.to_dict())
    else:
        abort(404)
