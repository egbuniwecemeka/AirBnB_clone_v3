#!/usr/bin/python3
""" view for state objects handling all RESTful APIs """

from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state_objs():
    """ Retrieves the list of all State objects """

    state_objs = storage.all(State).values()

    states_list = []

    for state in state_objs:
        states_list.append(state.to_dict())

    return jsonify(states_list)


@app_views.route('/states/<int:states_id>', methods=['GET'],
                 strict_slashes=False)
def state_obj(states_id):
    """ Retrieves a State object """
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Deletes a State object """
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    storage.delete(state)
    storage.save()

    return make_response(jsonify({}), 200)
