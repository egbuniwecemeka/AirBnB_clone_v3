#!/usr/bin/python3
""" view for state objects handling all RESTful APIs """

from api.v1.views import app_views
from models import storage
from flask import jsonify, request, make_response


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states_obj():
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


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """ Posts/creates a state  """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()

    new_state = State(**data)
    new_state.save()

    return make_response(jsonify(new_state.to_dict()), 201)
