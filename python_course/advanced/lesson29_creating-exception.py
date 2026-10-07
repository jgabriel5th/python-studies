# Creating Exceptions in Python Object-Oriented
# In order to create an Exception in Python, it's necessary
# to inherit from some exception of the language.
# The doc recommendation is to inherit from Exception.
# https://docs.python.org/3/library/exceptions.html
# Creating exceptions(common to put Error in the end)
# raising(raise) / throwing(throw) exceptions
# Rethrowing exceptions
# Adding notes in exceptions(3.11.0)
class MyError(Exception):
    pass

class AnotherError(Exception):
    pass

def raising():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Note 1')
    raise exception_

try:
    raising()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError('Rethrowing again')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('One more note')
    raise exception_ from error # rethrowing exception