from post import PostFactory
from Observer import Member


class User(Member):
    def __init__(self, username, password):
        super().__init__()
        # Initialize a new user.
        self.number_of_posts = 0
        self.number_of_followers = 0
        self.username = username
        self.password = password
        self.logged_in = True
        self.followers = set()
        self.following = set()
        self.notifications = []

    def follow(self, user):
        if user.logged_in is False or user == self:
            raise PermissionError("User is not logged in or trying to follow himself.")
        if user not in self.following:
            self.following.add(user)
            user.followers.add(self)
            user.number_of_followers += 1
            print(f"{self.username} started following {user.username}")

    def unfollow(self, user):
        if self.logged_in is False or user == self:
            raise PermissionError("User is not logged in or trying to unfollow himself.")
        if user in self.following:
            self.following.remove(user)
            if self in user.followers:
                user.followers.remove(self)
                user.number_of_followers -= 1
            print(f"{self.username} unfollowed {user.username}")

    def publish_post(self, post_type, *args, **kwargs):
        if self.logged_in is False:
            raise PermissionError("User is not logged in.")
        post = PostFactory.create_post(post_type, self, *args, **kwargs)
        self.number_of_posts += 1
        for follower in self.followers:
            follower.update(f"{self.username} has a new post")
        print(str(post))
        return post

    def print_notifications(self):
        # Print all notifications for the user.
        print(f"{self.username}'s notifications:")
        for notification in self.notifications:
            print(notification)

    def __str__(self):
        return (f"User name: {self.username}, Number of posts: "
                f"{self.number_of_posts}, Number of followers: {self.number_of_followers}")
