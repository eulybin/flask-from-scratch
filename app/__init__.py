from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

    db.init_app(app)

    with app.app_context():
        from . import models

        db.create_all()

    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
