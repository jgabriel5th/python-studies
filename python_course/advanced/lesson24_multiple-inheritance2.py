# Multiple Inheritance - Object-Oriented Python
# It means that in Python, a class can extend several
# other classes.
#
# Simple Inheritance:
# Animal -> Mammal -> Human -> Person -> Client
#
# Multiple Inheritance and mixes:
# Log -> FileLog
# Animal -> Mammal -> Human -> Person -> Client
# Client(Person, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# method -> speak
#           A
#         /   \
#        B    C # Diamond Problem
#        \   /
#          D
#
# Python 3 uses C3 superclass linearization
# to generate the mro(method resolution order).
# It's not necessary to be studied(complex)
#
# In order to know the method resolution order
# It can be used the class method Class.mro()
# Or the attribute __mro__ (Dunder - Double Underscore)
class A:
    ...

    def who_am_i(self):
        print('A')

class B(A):
    ...

    def who_am_i(self):
        print('B')
class C(A):
    ...

    def who_am_i(self):
        print('C')
class D(B, C):
    ...

    def who_am_i(self):
        print('D')


d = D()
d.who_am_i()
# print(D.__mro__)
print(D.mro())