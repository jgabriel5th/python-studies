from abc import ABC, abstractmethod
'''
Dependency Inversion Principle: it's a principle used to make a high-level class independent from low-level classes
and make that class depend only by abstractions.

Problematic Example:
class EmailService: # <- Low-level class
    def send(self, message):
        print(f"Email sent: {message}")


class Order: # <- High-level class
    def __init__(self):
        self.email_service = EmailService() # It depends directly on the low-level class.

    def FinishOrder(self):
        self.email_service.send("Order finished!")


If a new feature is going to be added in the future will also break the Open-Closed Principle by changing the Order class.
'''
# Solution:
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailService(Notifier):
    def send(self, message):
        print(f'Email sent: {message}')
    

class SMSService(Notifier):
    def send(self, message):
        print(f'SMS sent: {message}')


class Order: # Now the high-level class doesn't depend on the low-level classes but abstractmethod.
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    
    def FinishOrder(self):
        self.notifier.send("Order finished!")


email = EmailService()
order = Order(email) # <- Dependency injection
order.FinishOrder()