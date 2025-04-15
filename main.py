# main.py

from user_manager import UserManager
from login import login
from register import register
from search import search_user

def main():
    um = UserManager()
    
    # Registro de usuarios
    register(um, "alice", "password123")
    register(um, "bob", "securepass")
    
    # Intentos de login
    login(um, "alice", "password123")
    login(um, "bob", "wrongpass")
    
    # Actualización de datos (método update_user se modificará en ramas feature)
    um.update_user("alice", {"email": "alice@example.com"})
    
    # Búsqueda de usuarios
    results = search_user(um, "ali")
    print("Search results:", results)
    
    # Eliminación de usuario
    um.delete_user("bob")

    if True:
        if True:
            if True
                pass
    
if __name__ == "__main__":
    main()
