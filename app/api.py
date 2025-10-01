from flask import Blueprint, request, jsonify, abort
from .models import User
from . import db

api_bp = Blueprint("api", __name__)


@api_bp.get("/users")
def get_all_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@api_bp.post("/users")
def create_user():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@api_bp.delete("/users/<int:user_id>")
def delete_user(user_id):
    user_to_delete = User.query.get(user_id)
    if not user_to_delete:
        abort(404, "User was not found.")
    db.session.delete(user_to_delete)
    db.session.commit()
    return {"message": "User was successfully deleted."}
