#!/usr/bin/python3
""" view of City objects that handles all default RESTFUL API actions """

from models.city import City
from models.state import State
from api.v1.views import app_views
from models import storage
from flask import abort

@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities():
    """ Retrieves list of all City objects """
    state = storage(State, state_id)
    all_cities = []
    if not state:
        abort(404)

    for city in state.cities:
        all_cities.append(city)

    return jsonify(all_cities.to_dict())
