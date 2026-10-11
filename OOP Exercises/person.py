class Person:
    def __init__(self, name: str, age: int):
        self._validate(name, age)
        self.name = name
        self.age = age

    @staticmethod
    def _validate(name, age):
        if not isinstance(name, str):
            raise TypeError('Name must be str')
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError('Age must be int')
        if not name.strip():
            raise ValueError('Name cannot be empty')
        if age < 0:
            raise ValueError('Negative numbers are not allowed')

    def introduce(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old"

newt = Person('John', 1)
oliver = Person('Oliver', 22)
print(newt.introduce())

with open('explanation.txt', 'w') as file:
    file.write('The reason for the existence of this directory is basically because\n' \
    'I want to practice Object-Oriented Programming with some exercises since I have been watching ' \
    'just lessons of this paradigm.\nThe exercises will consist from the most basic ' \
    'such as creating a class Person to a LOG system.')
    file.close()