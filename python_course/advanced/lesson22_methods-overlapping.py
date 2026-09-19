# super() is the super class in the sub class
# Main class (Person)
#   -> super class, base class, parent class
# Children classes (Client)
#   -> sub class, child class, derived class

# class MyString(str):
#     def upper(self): # method overlapping
#         print('CALLED UPPER')
#         return1 = super(MyString, self).upper()
#         print('AFTER UPPER')
#         return return1

# name = MyString('Newton')
# print(name.upper())

class A:
    attribute_a = 'value a'
    def __init__(self, attribute):
        self.attribute = attribute

    def method(self):
        print()
        print('A')

    def method2(self):
        print('Method A')
        print()

class B(A):
    attribute_b = 'value b'

    def __init__(self, attribute, other_thing):
        super().__init__(attribute)
        self.other_thing = other_thing

    def method(self):
        print('B')

    def method2(self):
        print('Method B')
        print()

class C(B):
    attribute_c = 'value c'
    def __init__(self, attribute, other_thing, another_thing):
        super().__init__(attribute, other_thing)
        self.another_thing = another_thing
        

    def method(self):
        super(B, self).method() # A
        super(B, self).method2() # A
        super().method() # B
        super().method2() # B
        print('C')
        print('Method C')

c = C('Attribute', 'Anything', 'Another')
print(c.attribute, c.other_thing, c.another_thing)