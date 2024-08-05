#!/usr/bin/python3

""" Routing blueprint object to check app status """

from flask import Flask
from . import app_views


# Routes to a flask blueprint
@app_views.route('/status', methods=['GET'])
def get_status():
    """ Returns json dict response of app status """
    return jsonify(status='OK')
