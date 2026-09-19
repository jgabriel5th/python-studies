# Simple inheritance - Relationships between classes
# Association - use
# Aggregation - has
# Composition - own
# Inheritance - It is one

# Inheritance or Composition

# Main class (Person)
#   -> super class, base class, parent class
# Children classes (Client)
#   -> sub class, derived class, child class

# Every class inherits from a buil-in object in Python
# It's possible to see it using help(ClassName)
class Person:
    cpf = '123'
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def speak_name_class(self):
        print('Person class method')
        print(self.name, self.lastname, self.__class__.__name__)
        print()

class Client(Person): # Inheritance
    def speak_name_class(self):
        print('Client class method')
        print(self.name, self.lastname, self.__class__.__name__)
        print()

class Student(Person):
    cpf = '1234'
    ...

c1 = Client('John', 'Gabriel')
c1.speak_name_class()
s1 = Student('Abraham', 'Norton')
s1.speak_name_class()
print(c1.cpf)
print(s1.cpf)

# Method resolution order(the same applies to attributes):
# Child class
# Parent class
# builtins.object