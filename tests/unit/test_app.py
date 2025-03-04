from flask import Flask

from app import app


def test_flask_app_is_flask_instance() -> None:
    assert isinstance(app, Flask)
