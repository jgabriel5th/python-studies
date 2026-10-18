import math
class Rectangle:
    def __init__(self, width: float, length: float):
        self._validate(width, length)
        self.width = width
        self.length = length

    @staticmethod
    def _validate(width, length):
        if any(not isinstance(value, (float, int)) or isinstance(value, bool) for value in (width, length)):
            raise TypeError('Value must be a number')
        if any(value <= 0 or not math.isfinite(value) for value in (width, length)):
            raise ValueError('Negative number/infinite number are not allowed')
        
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        if self.width == self.length:
            return 'It is square'
        return 'It is rectangle'

rectangle = Rectangle(6, 1)
print(rectangle.area())
print(rectangle.perimeter())
square = Rectangle(5, 5)
print(square.is_square())
print(square.area())
print(square.perimeter())