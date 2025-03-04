from http import HTTPStatus
from flask.testing import FlaskClient
from pytest import fixture
from app.main import app

@fixture
def client() -> FlaskClient:
    return app.test_client()

def test_add_user(client: FlaskClient) -> None:
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    response = client.post("/users", json=user_data)
    assert response.status_code == HTTPStatus.CREATED

def test_get_user(client: FlaskClient) -> None:
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    client.post("/users", json=user_data)
    response = client.get("/users/1")
    assert response.status_code == HTTPStatus.OK

def test_get_all_users(client: FlaskClient) -> None:
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    client.post("/users", json=user_data)
    response = client.get("/users")
    assert response.status_code == HTTPStatus.OK