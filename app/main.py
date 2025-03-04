from flask import Flask, request
from flask.typing import ResponseValue
from app.controllers import UserController
from app.repositories import UserRepository

app = Flask(__name__)
repository = UserRepository()
controller = UserController(repository)


@app.get("/users")
def get_users() -> ResponseValue:
    try:
        controller.get_all()
    except ValueError:
        return "", 404
    return "", 200


@app.get("/users/<int:id>")
def get_user(id: int) -> ResponseValue:
    try:
        controller.get(user_id=id)
    except ValueError:
        return "", 404
    return "", 200

@app.post("/users")
def add_user() -> ResponseValue:
    user_data = request.get_json()
    required_fields = {"firstName", "lastName", "birthYear", "group"}
    if not user_data or not required_fields.issubset(user_data.keys()):
        return "Missing required fields", 400

    controller.add(user_data)
    return "", 201

@app.patch("/users/<int:id>")
def update_user(id: int) -> ResponseValue:
    try:
        user_data = request.get_json()
        controller.update(id, user_data)
    except ValueError:
        return "", 404
    return "", 200
