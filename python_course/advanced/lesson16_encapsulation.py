# Encapsulation (access modifiers: public, protected, private)
# Python DOESN'T HAVE access modifiers
# But it can be followed the following conversions:
#   (No underline) = public
#       It can be used anywhere
# _(one underline)  = protected
#       It must not be used out of the class
#       or its subclasses.
#__(two underlines) = private
#       "name mangling" in Python
#       _ClassName__name_attr_or_method
#       it MUST be used in the class
#       which was defined.
from functools import partial

class Example:
    def __init__(self):
        self.public = 'This is public'
        self._protected = 'This is protected'
        self.__private = 'This is private'

    def public_method(self):
        self.__private_method()
        self._protected_method()
        print(self.__private)
        print(self._protected)
        return 'This is a public method'

    def _protected_method(self):
        print('This is a protected method')
        return 'protected method'

    def __private_method(self):
        print('This is a private method')
        return 'private method'

example = Example()
# print(example.public)
print(example.public_method())