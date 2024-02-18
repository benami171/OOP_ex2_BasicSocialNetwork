# this class represent a social network with users and posts
# the design patt used here is the singleton pattern
# the class has a private constructor and a static method to get the instance of socialNetwork
# the class has sign up method to create a new user
# the class has log in and log out methods to log in and log out a user
from user import User


class SocialNetwork:
    __instance = None  # Class variable to store the single instance

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SocialNetwork, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name=""):
        if not hasattr(self, 'name'):
            self.name = name
            self.users = {}
            print(f"The social network {self.name} was created!")

    def sign_up(self, username, password):
        # Create a new user and add to the network.
        if username in self.users:
            return None  # User already exists
        user = User(username, password)
        self.users[username] = user
        return user

    def log_in(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            user.logged_in = True
            print(f"{username} connected")
            return user
        return None  # Invalid username or password

    def log_out(self, username):
        user = self.users.get(username)
        if user:
            user.logged_in = False
            print(f"{username} disconnected")
            return user
        return None  # User not found

    def __str__(self):
        user_strings = [str(user) for user in self.users.values()]
        users_info = '\n'.join(user_strings)
        return f"{self.name} social network:\n{users_info}"


