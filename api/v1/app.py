#!/usr/bin/python3
"""This script defines a Flask web application for an API."""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    if os.environ.get('HBNB_API_HOST'):
        host = os.environ.get('HBNB_API_HOST')
    else:
        host = "0.0.0.0"

    if os.environ.get('HBNB_API_PORT'):
        port = int(os.environ.get('HBNB_API_PORT'))
    else:
        port = 5000
    app.run(host=host, port=port, threaded=True)
