'''
Object-Oriented Programming:
It is one of the paradigms or patterns in programming, paradigms define how to write and structure the code.
Each paradigm has different functionalities and behaviors.

Examples of programming patterns:
- Structural programming
- Procedural programming
- Object-oriented programming
- Functional programming
- And there are more...
'''
# Python is an object-oriented programming language, and here's an example with type() function:
name = "João"
print(type(name)) # it returns <class 'str'>

'''
Classes and Objects:
- OOP is a paradigm that provides a means for structuring programs so that properties and behaviors are bundled into indivual objects.
- The two main concepts about OOP are Classes and Objects, in other words the variable 'name' is the object of the class 'string' at the most basic level.
- It allows developers to develop applications using the OOPs approach with a major focus on code reusability.
- Object-oriented programming is an approach for modeling concrete, real-world things, and relations between those things.
- OOP models real-world entities as programming objects that have some data associated with them and can perform certain functions.

The 4 Pillars of OOP:
Abstraction - It means to abstract only the details/data which might concern the user. The developer let the user abstract only the details that are required, the rest is hidden.
Encapsulation - It tries to encapsulate all the data as a single entity. Similarly a black box, where an input is passed, the box processes it and gives the result as an output
from the other end, therefore what happens in the black box is totally hidden. Encapsulation also hides the data.
Inheritance - A class can inherit various characteristics and capabilities from another class. It supports the concept of reusability, when a new a feature includes part from an
existing code, it can be derived from the existing one instead of developing from scratch.
Polymorphism - This word means "having many forms", so polymorphism is the ability of something to have more than one form. In programming, an operation may exhibit different behaviors
in different instances, these behaviors will depend upon the types of data used in the operation.

Building Blocks of OOP:
- Classes and Objects are the building blocks of the object-oriented system.
- Abstraction, Encapsulation, Inheritance, Polymorphism combined with Classes and Objects make an object-oriented program.

Classes:
- Like lists, tuples, dictionaries... Classes are advanced data structures to store, manipulate, and structure the data.
- Differently from lists, tuples, dictionaries and others data structures that can store only a few attributes, Classes is a type of user-defined structure that can store various attributes,
(Data - both primitive and user-defined) along with their functionalities, all together as a single unit.
- These attributes and their functionalities(behaviors) can be accessed via Objects.

Definition of a Class in OOP: "Blueprint to create objects."
- It's a user-defined prototype for an object that defines the set of attributes that characterize any object of the class.
- It's just like a prototype depending on which the real-world objects are created.
- An analogy: when a building is being planned to be created, the first to do is to create a blueprint of how the building would be. Depending upon that blueprint, real-world building structures
would be created that would be that same but with different attributes and functionalites such as colors, windows, interior, etc. At the most basic level, the base structure would be the same as
defined in the blueprint.

Objects:
- They are called as an instance of the class.
- An object contains two trings: Attributes(Data variables of the class) and Behaviors(Functions defined in the class).

Example:
- If the building is a class, therefore color, floors, flats, entrance, etc, would be the attributes, and isFinished(), isBusy(), flatAvailable(), etc would be its be behaviors that are the methods.
Each building would have all these data and behaviors and unique to themselves.

Defining a Class: Syntax
class className:
    #body of the class
- 'class' is the keyword used to define a class in Python.
- className is the name given to the class. It's similar to giving a name to a variable or a function, so it's important to choose a meaningful name.
- It's terminated with a semicolon.
- Inside the class, the attributes, the functions and the body of the class must be defined and indented.
'''

# Creating an Employee Class
class Employee:
    pass
 
 # The "pass" is just like a temporary placeholder until we add the required functionalities. The pass statement will be ignored by the Python interpreter and can be seen as a null statement.
 # Nothing will be returned in the output since at the moment the class is empty.

class Employee:
    empName = 'John'
    age = 30
    designation = 'Manager'

# It won't return any output considering that a class is just the description.
# It's necessary to create an object to access the attributes

'''
Declaring an Object: Syntax
objName = className()
- After it, it's possible to access the attributes and methods using the following syntax:
objName.attributeName
objName.methodName()
'''

# Creating an object of Employee Class
empOne = Employee()
print(empOne.empName, empOne.age, empOne.designation)

empTwo = Employee()
print(empTwo.empName, empTwo.age, empTwo.designation)

'''
Each object is a unique instance of the class and has its own attributes and behaviors, however the example above doesn't confirm it, because the attributes of the class Employee are quite rigid
so they return the same attributes and data for all the objects.
Thankfully, it's possible to solve this with the help of Constructors in Python.

Constructor:
- They're usually used for instantiating an object.
- Their function is to initialize(assign values) the data members of the class when an object of the class is created.

Syntax:
def __init__(self):
    # body of the constructor
- The attributes that all objects must have are defined in a method called __init__().
- Each time an object is created, __init__() sets the initial state of the object by assigning the values of the object's properties.
- __init__() initializes each new instance of the class.

Types of Python Constructors:
Default Constructor - It doesn't accept any arguments but 'self' which is a reference to the instance being constructed.
Syntax: objName = className()
- If a constructor is not provided in the syntax above, Python automatically assigns the default constructor to the class.

Parameterized Constructor - The first argument is 'self' and the rest of the arguments are provided which will be required attributes for the class.
Syntax: objName = className(parameterOne, parameterTwo,...)
- In this case, when an object is created with a parameterized constructor class, the arguments will need to be passed to the created object. 
It's quite similar how it's done in a function that accepts a parameter.
''' 

# Using __init__() <- Default Constructor:
class Employee:
    def __init__(self):
        self.empName = 'John'
        self.age = 30
        self.designation = 'Manager'

empOne = Employee()
print(empOne.empName)

# Just like the previous one, the attributes will be the same for all the objects.

# Now, making a dynamic class with Parameterized Constructor:
class Employee:
    def __init__(self, empName, age, designation):
        self.empName = empName
        self.age = age
        self.designation = designation

empOne = Employee("João", 21, "Developer")
empTwo = Employee("Raphael", 32, "Manager")
print(empOne.empName)
print(empTwo.empName)

class Professor:
    def __init__(self, proName, age, subject):
        self.proName = proName
        self.age = age
        self.subject = subject

prof1 = Professor("Francisco Coelho", 38, "Database")
prof2 = Professor("Ricardo", 40, "Computer Architecture")
prof3 = Professor("Luiz Lins", 40, "Back-End Framework")
prof4 = Professor("José Everton", 32, "Mobile Development")
print(prof1.proName, prof1.age, prof1.subject)

# Now, each object will have its unique values since they are being passed in their creation, directly inside the __init__ method.

'''
Self: it helps the class to individually recognize the instance(object) and accordingly pass the data to the object. It helps the class to know which object is requesting to
access the attributes and the methodss and depending upon the object parameters, the data is processed. In the previous example, it was written self.empName, self.age, self.designation which
will help the class to undersand which current object is accessing the attributes and accordingly return the output.
'''

# Adding Methods(Functions)
# It's nothing but simple Python function inside the class.

class Developer:
    totalDevelopers = 0

    def __init__(self, devName, age, level, salary):
        self.devName = devName
        self.age = age
        self.level = level
        self.salary = salary
        Developer.totalDevelopers = Developer.totalDevelopers + 1
    
    def getDevDetails(self): # returns all the details about the developers
        return self.devName, self.age, self.level, self.salary
    
    def updateSalary(self, newSalary): # accepts a parameter as newSalary and updates the self.salary to the passed value.
        self.salary = newSalary
        print('Salary Updated')
        return self.salary
    # Every method in a class has a first default parameter as 'self'.


'''
Class variables and Instance variables:
- totalDevelopers is not defined inside the __init__ and was not passed in the constructor because that value has to be calculated by the program and should not be passed at the time of object creation.
- Whenever a new object is created, the __init__ method is called, updating the value(totalDevelopers) by 1.
- It isn't possible to use 'self' in totalDevelopers, since this attribute doesn't depend on the object. It's possible to access it directly - Developer.totalDevelopers.
- Variables that are shared by all the objects are called Class variables and variable defined inside __init__ are called Instance variables.
'''

# Creating objects and seeing how these methods work
devOne = Developer('João Gabriel', 21, 'Junior', 3000)
print(devOne.getDevDetails())

devTwo = Developer('Guilherme', 20, 'Junior', 3000)
print(devTwo.getDevDetails())

devOne.updateSalary(3500)
print(devOne.getDevDetails())
print(Developer.totalDevelopers)

'''
More about Inheritance
- One class can inherit various characteristics(attributes) and capabilities(behavior/methods of a class) from another class.
- Reason: since there's a class Developer, if a creation of a class FrontEndDeveloper is considered it could just inherit all those data from the Developer class rather than creating again in the FrontEndDeveloper class.
Therefore, reusability.

Inheritance: Terminologies
Parent Class - It's the class the being inherited from the other classed. Also called the Base class.
Child Class - The class that inherits from another class. Also called a Derived class.

Inherintance: Syntax
class BaseClass:
   #body of the base class
class DerivedClass(BaseClass):
   #body of the derived class

- The name of the Parent Class is passed in the parenthesis while defining the Child Class.
'''

# Creating a Child Class: FrontEndDeveloper
class FrontEndDeveloper(Developer):
    pass

# Since the Child Class is empty an interesting thing will happen, it has only the access to the attributes and methods from the Parent Class even empty.
# If it had something in it, it would first create an object from it, but it doesn't so it will create an object using only the attributes and methods from the Parent Class.
# Trying it:
frntEnd1 = FrontEndDeveloper('Willian', 21, 'Junior', 3000)
print(frntEnd1.getDevDetails())

# Adding attributes and methods to the Child Class
class FrontEndDeveloper(Developer):

    def __init__(self, devName, age, level, salary, progLanguage):
        self.progLanguage = progLanguage # Creating a new one
        Developer.__init__(self, devName, age, level, salary) # Making a call to the constructor of the Parent Class within the constructor of the Child Class.
# Syntax: ParentClass.__init__(self, paremeter1, parameter2,...parameterN)
    def getLanguage(self):
        return f'The used programming language by the developer is {self.progLanguage}'

frntEndOne = FrontEndDeveloper('Filipe', 21, 'Junior', 3000, 'JavaScript')
print(frntEndOne.getDevDetails())
print(frntEndOne.getLanguage())

'''
Inheritance Types:
Single Inheritance - It's the inheritance done above. The derived class inherits from a single parent class.

Multilevel Inheritance - It's like a relationship representing a child and grandfather. 
Syntax:
class Employee:
    pass
class Intern(Employee)
    pass
class Bonus(Intern)
    pass
- The Bonus class cannot directly access the Employee class, however since it's inheriting the Intern class it can access the attributes and behaviors of both Employee
and the Intern class.

Multiple Inheritance - It's when a class can be derived from more than one base class. All the features of the base classes are inherited into the the derived class.
Syntax:
class Company:
    pass
class Employee:
    pass
class Intern(Company, Employee):
    pass

Hierarchical Inheritance - When more than one derived class is created from a single base class.
Syntax:
class Company
    pass
class Employee(Company)
    pass
class Intern(Company)
    pass
'''

'''
More about Polymorphism: someething can have many forms
- In OOP an object can have various forms in different situations depending upon the attributes and methods.
- A real-life example: Soccerplayer, in general the players of the team can have different forms such as forward player, midfield, goalkeeper(can use hands), defense and reserve(not playing).
- Just like the example above an object can have different forms and behave differently according to the situation.

The two types of Polymorphism in OOP: at the most basic level
Method Overloading - It's the situation where there are two methods of the same name but with different parameters in the same class.
Unfortunately, this method which is one of the most important forms of Polymorphism in OOP is NOT SUPPORTED in Python. Though it exists in other OOP programming languages like Java, C++, C#, etc, Python
doesn't support it.
Example: a method named area(), if the goal is to find the area of a retangle the parameters would be length and breath, now if the goal is to find the square the parameter would be just the side of the
square.
Method Overriding - It's when there are two methods with the same and the same parameters but in two different classes, it'll only come into the picture if the inheritance is involved, because the derived class
can override the methods from the parent class.
'''
# Trying to do an example of Method Overloading:
class Geometry:
    def __init__(self):
        self.name = "Name"
    
    def area(self, length, breadth):
        return f"The area of the retangle is: {(length * breadth)}" 
    
    def area(self, side):
        return f"The area of the square is: {(side * side)}" # This one overwrite the other, that's why it doesn't work. It's something of the programming language.
    
calc1 = Geometry()
print(calc1.area(8))

# Doing an example of Method Overriding:
class Phone:
    def __init__(self, number, color, brand):
        self.number = number
        self.color = color
        self.brand = brand
    
    def makingCall(self):
        return "Ring ring ring"
    
class Smartphone(Phone):
    def __init__(self, number, color, brand, processor):
        self.processor = processor
        Phone.__init__(self, number, color, brand)
    
    def makingCall(self):
        return "No ring ring anymore"

brick = Phone(41, "brown", "nokia")
redmi = Smartphone(82, "red", "Xiaomi", "Snapdragon")
print(brick.makingCall())
print(redmi.makingCall()) # <- Both methods have the same names and parameters but they do different things, cause' one is from the Base Class and the other is from the Child Class.

# OOP Branch