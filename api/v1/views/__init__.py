#!/usr/bin/python3

""" A Blueprint to a Flask instance """

from flask import Blueprint
# from api.v1.views.index import get_status, objs_num

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

from api.v1.views.index import *
