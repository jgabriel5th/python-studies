# Abstract classes - Abstract Base Class(ABC)
# ABCs are used as contracts for the new classes
# definion. They can force other classes to create
# concrete methods. They can have concrete methods
# by themselves as well.
# @abstractmethods are methods without body.
# The rule for abstract classes with abstract methods
# is that they CANNOT be instantiated directly.
# Abstract methods MUST be implemented in the subclasses(@abstractmethod).
# An abstract class in Python has its own metaclass being ABCMeta.
# It's possible to create @property, @setter, @classmethod, @staticmethod and @method
# as abstracts, in order for it, it's necessary to use @abstractmethod as inner decorator.
from abc import ABC, ABCMeta, abstractmethod

# class Log(metaclass=ABCMeta): # First way

class Log(ABC): # Second way
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}') # Concrete method

    def log_success(self, msg):
        return self._log(f'Success: {msg}') # Concrete method


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_success('Hi')