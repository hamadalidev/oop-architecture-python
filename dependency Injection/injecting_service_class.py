class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")

class UserService:
    def __init__(self, logger: Logger):  # Injecting Logger class
        self.logger = logger

    def create_user(self, username):
        self.logger.log(f"User '{username}' created successfully!")

# Instantiate Logger
logger = Logger()

# Inject Logger into UserService
user_service = UserService(logger)

# Call method
user_service.create_user("JohnDoe")
