#!/usr/bin/python3
"""This script defines a Flask view function for the API."""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """Provides a route to check the status of the API."""
    return jsonify(status="OK")
