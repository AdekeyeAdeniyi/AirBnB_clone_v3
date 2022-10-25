#!/usr/bin/python3
""" Flask Application Setup """
from flask import Flask
from os import getenv
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')

    app.run(
        host=host or "0.0.0.0",
        port=port or "5000",
        debug=True,
        threaded=True
    )
