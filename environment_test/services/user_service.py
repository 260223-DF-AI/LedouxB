from environment_test.util import format_name, is_valid_email, setup_logger
from environment_test.util.validators import is_valid_age

logger = setup_logger(__name__)

class User:
    """ Represent the user in the system """

    def __init__(self, first_name: str, last_name: str, email: str, age: int):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.age = age

    def validate(self):
        errors = []
        if not is_valid_email(self.email):
            errors.append("email is not valid")
        if not is_valid_age(self.age):
            errors.append("age is not valid")
        return errors
    
    def __str__(self):
        return f'{self.first} {self.last} ({self.age}), {self.email}'

def create_user (first: str, last: str, email: str, age: int):
    """Factory function to create and validate a user."""
    user = User(first, last, email, age)
    errors = user.validate()
    if errors:
        logger.error(f'Error creating user {email}: {', '.join(errors)}')
        raise ValueError(f"User validation failed: {errors}")
    logger.info(f"Created user {email}")
    return user