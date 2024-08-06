#!/usr/bin/python3
""" view for state objects handling all RESTful APIs """

from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_view.route('/states', methods=['GET'], strict_slashes=False)
def state_objs():
    """ Retrieves the list of all State objects """

    state_objs = storage.all(State).values()

    states_list = []

    for state in state_objs:
        states_list.append(state.to_dict())

    return jsonify(states_list)
