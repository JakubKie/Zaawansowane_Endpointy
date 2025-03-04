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

def test_update_user(client: FlaskClient) -> None:
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    client.post("/users", json=user_data)
    update_data = {"lastName": "Smith"}
    response = client.patch("/users/1", json=update_data)
    assert response.status_code == HTTPStatus.OK

def test_delete_user(client: FlaskClient) -> None:
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    client.post("/users", json=user_data)
    response = client.delete("/users/1")
    assert response.status_code == HTTPStatus.NO_CONTENT

def test_add_user_with_incomplete_data(client: FlaskClient) -> None:
    user_data = {"firstName": "John", "lastName": "Doe", "group": "user"}
    response = client.post("/users", json=user_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_get_nonexistent_user(client: FlaskClient) -> None:
    response = client.get("/users/999")
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_update_nonexistent_user(client: FlaskClient) -> None:
    update_data = {"lastName": "Smith"}
    response = client.patch("/users/999", json=update_data)
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_delete_nonexistent_user(client: FlaskClient) -> None:
    response = client.delete("/users/999")
    assert response.status_code == HTTPStatus.NOT_FOUND