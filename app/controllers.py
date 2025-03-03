from app.repositories import UserRepository

class UserController:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get(self, user_id: int) -> dict:
        return self.repository.get(user_id=user_id)