# Class Relationships: association, aggregation and composition
# Composition is an aggregation specialization.
# But in it, when the "dad" object is deleted, all
# the children objects references are deleted as well.
class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def insert_address(self, street, number):
        self.addresses.append(Address(street, number)) # Composition

    def list_addresses(self):
        for address in self.addresses:
            print(address.street, address.number)

class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number


client1 = Client('Abraham')
client1.insert_address('Boulevard', 170)
client1.list_addresses()
del client1