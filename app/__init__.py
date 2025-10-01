from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    return app
