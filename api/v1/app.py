#!/usr/bin/python3
""" A flask application """

from flask import Flask, jsonify

# Create a Flask instance
app = Flask(__name__)


# Route to a URL that triggers a function
@app.route('/api/v1/status', strict_slashes=False)
def get_status():
    return jsonify(status='OK')


if __name__ == "__main__":
    app.run(debug=True)
