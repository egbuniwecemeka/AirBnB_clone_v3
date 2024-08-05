#!/usr/bin/python3

""" A Blueprint to a Flask instance """

from flask import Blueprint

# Blueprint instance with name and set url_prefix
app_views = Blueprint("api_v1_bp", __name__, url_prefix="/api/v1")
