# Decorators functions and decorators with classes
def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls


# class MyReprMixin: # To use with inheritance
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr
    
@add_repr
class Team:
    def __init__(self, name):
        self.name = name

@add_repr
class Planet:
    def __init__(self, name):
        self.name = name


brazil = Team('Brazil')
portugal = Team('Portugal')


earth = Planet('Earth')
mars = Planet('Mars')

print(brazil)
print(portugal)

print(earth)
print(mars)