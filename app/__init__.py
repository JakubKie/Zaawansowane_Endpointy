from flask import Flask
from app.repositories import UserRepository
from app.controllers import UserController
app = Flask(__name__)
repository = UserRepository()
controller = UserController(repository)
