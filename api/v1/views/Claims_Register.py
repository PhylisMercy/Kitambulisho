# Privileged API that enables to check all turned in Lost ID's @ Registered Huduma Station across all Counties.
# todo Add Endpoint that is passed the kitambulisho ID that is yet to be signed off and it will return the register's
# row ID
# Grab the claims Register Per Place & Globally for Administration Purposes.

import os

from flask import jsonify, escape, abort, request

from api.v1.views import app_views
from models import storage, \
    County, Kitambulisho_Collection_Register

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


@app_views.route('/claims_register', strict_slashes=False)
def get_claims_registers():
    """
    Returns the Global List of all turned in Vitambulisho At all collection Stations
    curl -X GET http://0.0.0.0:5000/api/v1/claims_register/
    """
    temp = list()
    if STORAGE_TYPE == "db":
        states = storage.all('Kitambulisho_Collection_Register')
    else:
        states = storage.all(Kitambulisho_Collection_Register)
    for key, val in states.items():
        temp.append(val.to_dict())
    # return render_template('7-states_list.html', states=states)
    return jsonify(temp)

@app_views.route('/claims_register/<claims_register_id>', strict_slashes=False)
def get_claims_register(claims_register_id):
    """
    Returns all the Turned in Vitambulisho at Huduma/Kitambulisho Collection Stations.
    curl -X GET http://0.0.0.0:5000/api/v1/claims_register/<claims_register_id
    """
    if claims_register_id:
        if STORAGE_TYPE == "db":
            claims_register = storage.get('Kitambulisho_Collection_Register',escape(claims_register_id))
        else:
            claims_register = storage.get(Kitambulisho_Collection_Register, escape(claims_register_id))

        if not claims_register:
            abort(404)
        return jsonify(claims_register.to_dict())

@app_views.route('/claims_register/<claims_register_id>',
                 strict_slashes=False,
                 methods=['DELETE'])
def del_claims_register(claims_register_id):
    """ Function returns list of cities by states and
    displays/renders them in a html document.
    when no get parameter is provided it will list all available
    states.
    When a state_id is provided it will list all cities within than state
    When a non_existent state_id is provided (url/states/<invalid_state_id>
    the page displays "Not found!"
    """
    if claims_register_id:
        if STORAGE_TYPE == "db":
            del_obj = storage.get("Kitambulisho_Collection_Register", escape(claims_register_id))
        else:
            # Handles File Storage
            # storage.get return an object dictionary else None
            del_obj = storage.get(Kitambulisho_Collection_Register, escape(claims_register_id))
        if del_obj:
            # storage.delete returns true on success else false
            del_status = storage.delete(del_obj)
            if del_status:
                return jsonify({})
            else:
                abort(404)
        else:
            abort(404)

""" To Post to Claims Register
 use the endpoint
 curl -X POST http://0.0.0.0:5001/api/v1/places/<place_id>/amenities/<amenity_id>
 """

@app_views.route('/claims_register/<claims_register_id>',
                 strict_slashes=False, methods=['PUT'])
def update_claims_register_transfer(claims_register_id):
    """  Enables for Register Update in Case of Kitambulisho Transfer to Other Huduma Center.
     curl -X POST http://0.0.0.0:5001/api/v1/claims_register/<claims_register_id> -H "Content-Type: application/json" -d '{"collection_station_id": "<transfer_station>"}'
    # todo: When a kitambulisho tranfer occurs post the from and to stations to a tranfers db table.
    #this will help to track the to & from & should have a bool status column to verify document arrival
    """
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    ignore_fields = ['kitambulisho_id'] # You cannot Update the Kitambulisho_id
    status = storage.update(Kitambulisho_Collection_Register, claims_register_id, req_json, ignore_fields)

    if status:
        return jsonify(status.to_dict())
    else:
        abort(404)



