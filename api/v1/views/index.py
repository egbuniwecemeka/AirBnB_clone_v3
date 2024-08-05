#!/usr/bin/python3

""" Routing blueprint object to check app status """

from flask import Flask, jsonify
from api.v1.views import app_views


# Routes to a flask blueprint
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ Returns json dict response of app status """
    return jsonify({'status': 'OK'})
