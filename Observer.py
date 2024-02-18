from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def notify(self, message, user):
        pass


class Member(ABC):
    @abstractmethod
    def update(self, message):
        pass










