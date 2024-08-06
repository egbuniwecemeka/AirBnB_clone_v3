#!/usr/bin/python3
""" view of City objects that handles all default RESTFUL API actions """

from models.city import City
from models.state import State
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify, make_response


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """ Retrieves list of all City objects """
    state = storage.get(State, state_id)
    all_cities = []
    if not state:
        abort(404)

    for city in state.cities:
        all_cities.append(city.to_dict())

    return jsonify(all_cities)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """  Retrieves a City object  """

    city = storage.get(City, city_id)
    if not city:
        abort(404)

    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """ Deletes a City object of city_id """
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    storage.delete()
    storage.save()

    return make_response(jsonify({}), 200)
