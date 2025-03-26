# user_manager.py

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = {"password": password, "data": {}}
        return True

    def update_user(self, username, data):
        # Este método será modificado por dos desarrolladores para simular conflicto.
        if username in self.users:
            self.users[username]["data"].update(data)
            return True
        return False

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        return False

    def get_user(self, username):
        return self.users.get(username, None)


 def