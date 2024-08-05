#!/usr/bin/python3

""" Routing blueprint object to check app status """

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


# Routes to a flask blueprint
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ Returns json dict response of app status """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def objs_num():
    """ Returns the number of objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}

    for i in range(len(classes)):
        count = storage.count(classes[i])
        num_objs[names[i]] = count

    return jsonify(num_objs)
