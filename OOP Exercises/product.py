import math
class Stock:
    def __init__(self, name):
        self.name = name
        self._product = []

    def list_product(self):
        for index, product in enumerate(self._product):
            return f'Product {index+1}: {product.name}\nPrice: {product.price}\nQuantity: {product.quantity}'
    def insert_product(self, *product):
        self._product += product

    def remove_product(self, product):
        self._product.remove(product)

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self._validate(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def _validate(name, price, quantity):
        if not isinstance(name, str) or isinstance(name, bool):
            raise TypeError('Name must be string')
        if not name.strip():
            raise ValueError('Empty spaces are not allowed')
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError('Price must be a number')
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError('Quantity must be integer')
        if any(value < 0 for value in (price, quantity)):
            raise ValueError('Negative numbers are not allowed')
        if any(not math.isfinite(value) for value in (price, quantity)):
            raise ValueError('Infinite values are not allowed')
        
banana = Product('Banana', 2, 2)
apple = Product('Apple', 1, 1)
supermarket = Stock('Supermarket')
supermarket.insert_product(banana)
supermarket.insert_product(apple)
print(supermarket.list_product())
supermarket.remove_product(banana)
print(supermarket.list_product())