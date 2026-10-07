# Python Special Methods, Magic Methods or Dunder Methods
# Dunder = Double Underscore = __dunder__
# Old and useful: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self): # Used to show an object as a string
        return f'({self.x}, {self.y})'
    
    def __repr__(self): # Usually used for communicate other developers how the object is represented
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other

if __name__ == '__main__':
    p1 = Point(4, 3)
    p2 = Point(8, 4)
    p3 = p1 + p2
    print(p3)
    print('P1 is bigger than P2', p1 > p2)
    print('P2 is bigger than P1', p2 > p1)