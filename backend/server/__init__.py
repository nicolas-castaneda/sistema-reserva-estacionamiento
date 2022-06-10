from flask import (
    Flask,
    jsonify,
    abort,
    request
)
from flask_cors import CORS

from models import setup_db, Usuario, Auto, Estacionamiento, Reserva

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, max_age=10)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    

    return app