# login.py

from user_manager import UserManager

def login(user_manager, username, password):
    user = user_manager.get_user(username)
    if user and user.get("password") == password:
        print("Login successful!")
        return True
    print("Login failed!")
    return False
