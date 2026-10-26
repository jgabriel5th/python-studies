import math
class Person:
    def __init__(self, name, age, genre):
        self._validate(name, age, genre)
        self.name = name
        self._age = age
        self.genre = genre

    @staticmethod
    def _validate(name, age, genre):
        if any(not isinstance(value, str) for value in (name, genre)):
            raise TypeError('Name and genre must be string')
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError('Age must be a number')
        if any(not value.strip() for value in (name, genre)):
            raise ValueError('Empty space are not allowed')
        if age < 0 or not math.isfinite(age):
            raise ValueError('Negative/Infinite value not allowed')

    @property
    def age(self):
        return self._age

    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return f'{class_name}({class_dict})'

p1 = Person('Holmes', 38, 'Man')
print(p1)