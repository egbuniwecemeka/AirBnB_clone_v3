#!/usr/bin/python3
""" A flask application """

from flask import Flask
from api.v1.views import app_views

# Create a Flask instance
app = Flask(__name__)


def main_app():
    """ Registering blueprint with flask application """
    app.register_blueprint(app_views)

    return app


if __name__ == "__main__":
    app.run(debug=True)
