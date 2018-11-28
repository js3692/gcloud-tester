from flask import Flask
from flask import request


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def handler():
        return 'Ok'

    return app
