from post import PostFactory
from Observer import Member


class User(Member):
    def __init__(self, username, password):

        # Initialize a new user.
        self.number_of_posts = 0
        self.number_of_followers = 0
        self.username = username
        self.password = password
        self.logged_in = True
        self.followers = set()
        self.following = set()
        self.notifications = []

    def update(self, message):
        # Update the user with a new notification.
        self.notifications.append(message)

    def follow(self, user):
        if user not in self.following:
            self.following.add(user)
            user.followers.add(self)
            user.number_of_followers += 1
            print(f"{self.username} started following {user.username}")

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            if self in user.followers:
                user.followers.remove(self)
                user.number_of_followers -= 1
            print(f"{self.username} unfollowed {user.username}")

    def publish_post(self, post_type, *args, **kwargs):
        post = PostFactory.create_post(post_type, self, *args, **kwargs)
        self.number_of_posts += 1
        for follower in self.followers:
            follower.update(f"{self.username} has a new post")
        if post_type == "Text":
            print(f"{self.username} published a post:\n\"{args[0]}\"")
        elif post_type == "Image":
            print(f"{self.username} posted a picture")
        elif post_type == "Sale":
            print(
                f"{self.username} posted a product for sale:\nFor sale! {args[0]}, price: {args[1]}, pickup from: {args[2]}")
        print()
        return post

    # def like(self, post):
    #     # Like a post.
    #     if post.user != self:
    #         print(f"{self.username} liked {post.user.username}'s post")
    #         post.user.notify_like(self, post)
    #         return True
    #     return False

    # def comment_post(self, post, comment):
    #     # Comment on a post.
    #     if post.user != self:
    #         print(f"{self.username} commented on {post.user.username}'s post: {comment}")
    #         post.user.notify_comment(self, comment)
    #         return True
    #     return False

    def attach_follower(self, follower):
        # Attach a follower to the user.
        self.followers.add(follower)

    def detach_follower(self, follower):
        # Detach a follower from the user.
        self.followers.remove(follower)

    # def notify(self, notification):
    #     # Send a notification to the user.
    #     self.notifications.append(notification)
    #
    # def notify_like(self, user):
    #     # Send a notification about a like to the user.
    #     self.notifications.append(f"notification to {self.username}: {user.username} liked your post")
    #
    # def notify_comment(self, user, comment):
    #     # Send a notification about a comment to the user.
    #     self.notifications.append(f"notification to {self.username}: {user.username} commented on your post: {comment}")

    def print_notifications(self):
        # Print all notifications for the user.
        print(f"{self.username}'s notifications:")
        for notification in self.notifications:
            print(notification)

    def __str__(self):
        return (f"User name: {self.username}, Number of posts: "
                f"{self.number_of_posts}, Number of followers: {self.number_of_followers}")
