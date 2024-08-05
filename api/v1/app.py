#!/usr/bin/python3
""" A flask application """

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

# Create a Flask instance
app = Flask(__name__)

# Registering blueprint with flask application
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    if exception:
        print(f'An error occurred: {exception}')
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', 5000)),
            debug=True, threaded=True)
