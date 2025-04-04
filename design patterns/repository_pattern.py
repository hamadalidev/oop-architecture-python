# Fake database
fake_db = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

# Repository
class UserRepository:
    def get_all_users(self):
        return fake_db

    def get_user_by_id(self, user_id):
        return next((user for user in fake_db if user["id"] == user_id), None)

# Service Layer
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_user_details(self, user_id):
        user = self.repo.get_user_by_id(user_id)
        return f"User: {user['name']}" if user else "User not found"

# Usage
repo = UserRepository()
service = UserService(repo)

print(service.get_user_details(1))  # Output: User: Alice
