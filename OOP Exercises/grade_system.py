class Student:
    def __init__(self, name, age, genre, course):
        self.name = name
        self._age = age
        self.genre = genre
        self.course = course
        self._grades = []

    def insert_grade(self, *grades):
        self._grades += grades

    def list_grade(self):
        for item in self._grades:
            print(item.grade)

    def media(self):
        media = sum(i.grade for i in self._grades) / 2
        return media
    
    def check_approved(self):
        if Student.media(self) >= 7:
            return 'Approved'
        elif Student.media(self) < 7 and Student.media(self) >= 5:
            return 'Academic recovery'
        else:
            return 'Failed'


class Grade:
    def __init__(self, grade):
        self._grade = grade

    @property
    def grade(self):
        return self._grade
    


grade1 = Grade(10)
grade2 = Grade(4)
student = Student('John', 24, 'Man', 'Technology')
student.insert_grade(grade1, grade2)
student.list_grade()
print(student.check_approved())