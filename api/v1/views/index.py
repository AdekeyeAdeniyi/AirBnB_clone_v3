#!/usr/bin/python3xx
""" API Routes """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status_response():
    return jsonify(status='OK')
