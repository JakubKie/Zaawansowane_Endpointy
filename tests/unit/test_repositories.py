from pytest import raises
from app.repositories import UserRepository

def test_user_repository():
    repo = UserRepository()
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    user = repo.add(user_data)
    assert user["id"] == 1
    assert user["firstName"] == "John"

    retrieved_user = repo.get(1)
    assert retrieved_user == user

    updated_user = repo.update(1, {"lastName": "Smith"})
    assert updated_user["lastName"] == "Smith"

    repo.delete(1)
    with raises(ValueError):
        repo.get(1)