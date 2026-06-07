'''
Liskov Substitution Principle: it's a principle used to make sure a Child Class inherits the same methods from the Parent Class.
Problematic Example:
class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying")

    def deliverBachelorThesis(self):
        print(f"{self.name} is delivering their Bachelor's Thesis") <- That's the problem, normally only College Students(at least in Brazil) deliver this Thesis 

If the method above be implemented in the Parent Class, the Child Class below will inherit it and that's go against the Liskov Substitution Principle.
Of course, it's possible to create an exception in the Child Class, but that's not the best way according to this principle.      

class GraduateStudent(Student):
    def __init__(self, name, course):
        self.course = course
        Student.__init__(self, name)
    
    def study(self):
        print(f"{self.name} is stuyding {self.course}")


'''
# Solution:
class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying")


class CollegeStudent(Student):
    def __init__(self, name, course):
        self.course = course
        Student.__init__(self, name)

    def deliverBachelorThesis(self):
        print(f"{self.name} is delivering their Bachelor's Thesis") # Now, the method was implemented without touching the Parent Class.
    

class GraduateStudent(Student):
    def __init__(self, name, gradCourse):
        self.gradCourse = gradCourse
        Student.__init__(self, name)
    
    def study(self):
        print(f"{self.name} is stuyding {self.gradCourse}")

