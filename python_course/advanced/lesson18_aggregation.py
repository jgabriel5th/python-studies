# Class Relationships: association, aggregation and composition
# Aggregation is a more specialized form of association between 
# two or more objects. Each object will have its own independent life cycle.
# Usually it's a relationship one-to-many, where an object has one or many objects.
# The objects can live separately, but it could be a relationship where an object
# needs the other to do a specific task.
# (there are controversies regarding the definition of aggregation)
class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])

    def insert_products(self, *products):
        # self._products.extend(products) # Way 1
        self._products += products # Way 2

    def list_products(self):
        for product in self._products:
            print(product.name, product.price)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
p1, p2 = Product('Cookie', 2.40), Product('Coke', 2.0)
cart.insert_products(p1, p2)
cart.list_products()
