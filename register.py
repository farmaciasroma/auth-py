# register.py

from user_manager import UserManager

def register(user_manager, username, password):
    if user_manager.add_user(username, password):
        print("User registered successfully!")
        return True
    print("Registration failed: User already exists.")
    return False
