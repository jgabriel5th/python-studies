class Person:
    def __init__(self, name, age, genre):
        self.name = name
        self.age = age
        self.genre = genre

    def greeting(self):
        return f"Hello, I'm {self.name}"

    def list_person(self):
        return f'Name: {self.name}\nAge: {self.age}\nGenre: {self.genre}'

class Student(Person):
    def __init__(self, name, age, genre):
        super().__init__(name, age, genre)
        self._course = None
        self._college = None

    @property
    def course(self):
        return self._course
    
    @course.setter
    def course(self, course):
        self._course = course

    @property
    def college(self):
        return self._college
    
    @college.setter
    def college(self, college):
        self._college = college

class Course:
    def __init__(self, name):
        self.name = name

class College:
    def __init__(self, name):
        self.name = name


student = Student('John', 28, 'Man')
course = Course('Software Development')
college = College('Nassau')
student.course = course
student.college = college
print(student.name, student.college.name, student.course.name)
print(student.list_person())