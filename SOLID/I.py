from abc import ABC, abstractmethod
'''
Interface Segregation Principle: it's used to make small and specific interfaces instead of creating a generic one, because most of the classes won't use its methods.
Instead of forcing classes to use a generic interface(abstractmethod) that has methods which are useless for them, this principle recommends to create specifics interfaces.

Problematic Example:
class Employee(ABC):

    @abstractmethod
    def salary(self, value):
        pass
    
    @abstractmethod
    def comission(self, value2):
        pass
        
class Receptionist(Employee):
    def __init__(self, rname, age, gender):
        self.rname = rname
        self.age = age
        self.gender = gender
    
    def salary(self, value):
        print(f"{self.rname}'s salary is {value}")
    
    def comission(self, value2): <- Here's the problem, because a receptionist doesn't earn comission.
        print(f"Comission is: {value2}")

class Salesperson(Employee):
    def __init__(self, sname, age, sgender):
        self.sname = sname
        self.age = age
        self.sgender = sgender
    
    def salary(self, value):
        print(f"{self.sname}'s salary is {value}")
    
    def comission(self, value2):
        print(f"Comission is: {value2}")
'''
# Solution:
class Employee(ABC):

    @abstractmethod
    def salary(self, value):
        pass
    
class Comissionable(ABC):

    @abstractmethod
    def comission(self, value):
        pass

        
class Receptionist(Employee):
    def __init__(self, rname, age, gender):
        self.rname = rname
        self.age = age
        self.gender = gender
    
    def salary(self, value):
        print(f"{self.rname}'s salary is ${value}")
    

class Salesperson(Employee, Comissionable):
    def __init__(self, sname, age, sgender):
        self.sname = sname
        self.age = age
        self.sgender = sgender
    
    def salary(self, value):
        print(f"{self.sname}'s salary is ${value}")
    
    def comission(self, value2):
        print(f"{self.sname}'s comission is:${value2}")

receptionist = Receptionist("Nanda", 28, "Woman")
receptionist.salary(2000)

salesperson = Salesperson("Naldo", 34, "Man")
salesperson.comission(500)
salesperson.salary(2000)

# Now the classes have specific interfaces for them.