#!/usr/bin/python3

""" A Blueprint to a Flask instance """

from flask import Blueprint

# Wild import of api.v1.views.index package (as required)
from .index import *

# Blueprint instance with name and set url_prefix
app_views = Blueprint("api_v1_bp", __name__, url_prefix="/api/v1")
