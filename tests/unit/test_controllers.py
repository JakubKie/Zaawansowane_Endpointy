from unittest.mock import Mock
from pytest import fixture, raises
from app.controllers import UserController
from app.repositories import UserRepository

@fixture
def repository() -> Mock:
    return Mock(UserRepository)

@fixture
def controller(repository: Mock) -> UserController:
    return UserController(repository=repository)

def test_user_controller_get(controller: UserController, repository: Mock) -> None:
    user_id = 1
    user_data = {"id": 1, "firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    repository.get.return_value = user_data

    result = controller.get(user_id)
    assert result == user_data
    repository.get.assert_called_once_with(user_id=user_id)

def test_user_controller_get_not_found(controller: UserController, repository: Mock) -> None:
    user_id = 1
    repository.get.side_effect = ValueError("User not found")

    with raises(ValueError, match="User not found"):
        controller.get(user_id)
    repository.get.assert_called_once_with(user_id=user_id)

def test_user_controller_get_all(controller: UserController, repository: Mock) -> None:
    users = [{"id": 1, "firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}]
    repository.get_all.return_value = users

    result = controller.get_all()
    assert result == users
    repository.get_all.assert_called_once()

def test_user_controller_add(controller: UserController, repository: Mock) -> None:
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    created_user = {"id": 1, **user_data}
    repository.add.return_value = created_user

    result = controller.add(user_data)
    assert result == created_user
    repository.add.assert_called_once_with(user_data)