class UserAlreadyExistsError(Exception):
    """Raised when a user with that email already exists"""
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"User with email {email} already exists")

