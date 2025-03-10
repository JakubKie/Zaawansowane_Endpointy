class UserRepository:
    def __init__(self) -> None:
        self._users = {}
        self._next_id = 1

    def get(self, user_id: int) -> dict:
        if user_id not in self._users:
            raise ValueError("User not found")
        return self._users[user_id]

    def get_all(self):
        return self._users

    def add(self, user_data: dict) -> dict:
        user_id = self._next_id
        self._users[user_id] = {"id": user_id, **user_data}
        self._next_id += 1
        return self._users[user_id]

    def update(self, user_id: int, user_data: dict) -> dict:
        if user_id not in self._users:
            raise ValueError("User not found")
        self._users[user_id].update(user_data)
        return self._users[user_id]

    def delete(self, user_id: int) -> None:
        if user_id not in self._users:
            raise ValueError("User not found")
        del self._users[user_id]