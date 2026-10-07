# __new__ and __init__ in Python classes
# __new__ is the responsible method to create and
# return the new object. Because of this, new receives cls.
# __new__ MUST returns the new object
# __init__ is the responsible method to initialize
# the instance. Because of this, init receives self.
# __init__ MUST NOT return anything(NONE)
# object is the super class of a class.
class A:
    def __new__(cls, *args, **kwargs):
        print('Before creating the instance')
        instance = super().__new__(cls)
        print('After')
        instance.y = 213
        return instance

    def __init__(self, x):
        self.x = x
        print('I am the init')

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name!r}'
    
a = A(312)
print(a.y)