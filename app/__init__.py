from flask import Flask
from .routes import main as main_routes

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    app.register_blueprint(main_routes, debug=True)

    return app