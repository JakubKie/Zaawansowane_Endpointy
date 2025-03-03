class UserRepository:
    def __init__(self) -> None:
        self._users = {}
        self._next_id = 1

    def get(self, user_id: int) -> dict:
        if user_id not in self._users:
            raise ValueError("User not found")
        return self._users[user_id]