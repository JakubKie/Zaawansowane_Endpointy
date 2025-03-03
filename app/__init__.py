from flask import Flask
from repositories import UserRepository
from controllers import UserController
app = Flask(__name__)
repository = UserRepository()
controller = UserController(repository)
