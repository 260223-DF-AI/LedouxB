"""Entry point for the application"""

# absolute import
# from environment_test.services.user_service import create_user, User

# relative import
from .services.user_service import create_user, User
from environment_test import util


def main():
    """ Main function for execution. """
    print("Hello from main.py")

    logger = util.setup_logger(__name__)
    logger.info('Main started')

    try: #att
        user = create_user("Ben", "Ledoux", "benjamin728@revature.net", 23)
        print(f'Created user {user}')
        print(f'Email: {user.email}')
    except ValueError as e:
        print(f"ValueError creating user: {e}")
    except Exception as e:
        print(f"Exception creating user: {e}")
    
    try:
        user = create_user("Ben", "Ledoux", "bledouxatgmaildotcom", -23)
    except ValueError as e:
        print(f"ValueError creating user: {e}")
    logger.info("Main completed successfully!")


if __name__ == "__main__":
    main()