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

    def method(self):
        print('A')

class B(A):
    attribute_b = 'value b'

    def method(self):
        print('B')

class C(B):
    attribute_c = 'value c'

    def method(self):
        super().method()
        print('C')

c = C()
print(c.attribute_a)
print(c.attribute_b)
print(c.attribute_c)
c.method()