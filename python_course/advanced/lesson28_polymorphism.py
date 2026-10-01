# Polymorphism in Python Object-Oriented
# Polymorphism is the principle which allows
# sub-classes from a same superclass have
# the same method(with the same signature)
# but with different behaviours.
# Method signature = Same name and parameter
# quantity(return doesn't make part of the signature)
# Opinion + principles that count:
# Method signature: name, parameters and same return
# SO"L"ID
# Liskov Substitution Principle
# Superclass's objects must be replaceable by objects
# of a subclass without breaking the application.
# Method overload = Python doesn't support
# Method override = Python supports
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self) -> bool: ... # TypeAnnotations/TypeHints: used to indicate
    # the expected value from a variable, function parameter or function return.

class EmailNotification(Notification):
    def send(self) -> bool:
        print('E-mail: sending -', self.message)
        return True

class SMSNotification(Notification):
    def send(self) -> bool:
        print('SMS: sending - ', self.message)
        return False


def notificate(notification: Notification):
    sent_notification = notification.send()

    if sent_notification:
        print('Notification was sent')
    else:
        print('Notification was not sent')

email_notification = EmailNotification('Testing e-mail')
notificate(email_notification)

sms_notification = SMSNotification('Testing SMS')
notificate(sms_notification)