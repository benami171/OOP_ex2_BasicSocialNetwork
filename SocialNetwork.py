from user import User


class SocialNetwork:
    __instance = None  # Class variable to store the single instance
    """ This method is called before __init__ when an object is created.
        The Singleton pattern ensures that only one instance of the SocialNetwork class exists.
        If an instance already exists, it returns that instance. If not, it creates a new one.
        """
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SocialNetwork, cls).__new__(cls)
        return cls.__instance

    """ The name of the social network will be set only once,
        when the first instance of the class is created, 
        so if someone tries to create a new instance we check if the name is already set"""
    def __init__(self, name=""):
        if not hasattr(self, 'name'):
            self.name = name
            self.users = {}
            print(f"The social network {self.name} was created!")

    def sign_up(self, username, password):
        # Create a new user and add to the network.
        if username in self.users:
            raise ValueError("Username already exists")
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
        return f"{self.name} social network:\n{users_info}\n"


