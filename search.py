# search.py

def search_user(user_manager, search_term):
    results = []
    for username in user_manager.users.keys():
        if search_term.lower() in username.lower():
            results.append(username)
    return results
