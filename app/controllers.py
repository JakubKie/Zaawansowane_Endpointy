from app.repositories import UserRepository

class UserController:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get(self, user_id: int) -> dict:
        return self.repository.get(user_id=user_id)

    def get_all(self) -> list:
        return self.repository.get_all()

    def add(self, user_data: dict) -> dict:
        return self.repository.add(user_data)

    def update(self, user_id: int, user_data: dict) -> dict:
        return self.repository.update(user_id, user_data)

    def delete(self, user_id: int) -> None:
        self.repository.delete(user_id)