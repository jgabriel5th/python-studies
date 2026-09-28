# abstractmethod for any decorated method.
# It's possible to create @property @property.setter @classmethod
# @staticmethod and ordinary methods as abstracts, for that
# it's necessary to use @abstractmethod as inner decorator.
# Foo - Bar are the most used words as placeholder
# for words that can change in coding.
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('I am useless')

    # @property # If AbstractFoo property name is an abstractmethod.
    # def name(self):
    #     return self._name

    # @name.setter # If AbstractFoo property name is an abstractmethod.
    # def name(self, name):
    #     self._name = name

    @AbstractFoo.name.setter # If AbstractFoo name.setter is an abstractmethod
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)