class User:
    def __init__(self, username):
        self.username = username


    # Encapsulation: Getter
    def get_username(self):
        return self.username


class Admin(User):
    # Inheritance: Admin is a User with additional privileges
    pass


def authenticate(username, password, user_data):
    if username in user_data and user_data[username] == password:
        if username == "Rabat":
            return Admin(username)
        else:
            return User(username)
    return None
