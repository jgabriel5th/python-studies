from abc import ABC, abstractmethod # First part of the solution
'''
Open-Closed Principle: it's a principle used in order to avoid a class to be changed every time a new feature is implemented. If a class is changed whenever a new feature
comes, it'll become complex and hard to handle.

Problematic Example:
class DiscountCalculator:
    def calculate(self, client_type, value):
        if client_type == "common":
            return value * 0.05
        elif client_type == "premium":
            return value * 0.10
        elif client_type == "vip":
            return value * 0.20

If a new client type needs to be implemented, like "gold", it'll be necessary to put another elif and that's ugly.

Solution:
'''

class Discount(ABC):
    @abstractmethod
    def calculate(self, value):
        pass

class CommonDiscount(Discount):
    def calculate(self, value):
        return value * 0.05

class PremiumDiscount(Discount):
    def calculate(self, value):
        return value * 0.10

class GoldDiscount(Discount): # The new"gold" one implemented apart the main class.
    def calculate(self, value):
        return value * 0.15

class VipDiscount(Discount):
    def calculate(self, value):
        return value * 0.20

class DiscountCalculator: # Main class.
    def calculate(self, discount: Discount, value):
        return discount.calculate(value)
    
calculator = DiscountCalculator()
vip_client = VipDiscount()
discount = calculator.calculate(vip_client, 1000)
print(f'Discount: ${discount:.2f}')