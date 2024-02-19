class Sender:
    @staticmethod
    def notify(user, recipient, flag):
        if flag == "like":
            recipient.update(f"{user.username} liked your post")
        if flag == "comment":
            recipient.update(f"{user.username} commented on your post")


class Member:
    def __init__(self):
        self.notifications = []

    def update(self, message):
        self.notifications.append(message)
