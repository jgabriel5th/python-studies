# Context Manager with classes
# It's possible to implement your own protocols
# by implementing the dunder methods that Python
# is going to use.
# This is called Duck typing. A concept related
# with dynamic typing which Python is not interested
# in the type, but if some methods exist in your object
# so that it can work appropriately.
# Duck Typing:
# When I see a bird, walks as a duck, swims as a duck
# and quacks as a duck, I call that bird as a duck.
# For creating a context manager, the methods __enter__ and __exit__
# must be implemented.
# The __exit__ method will receive the exception class, the exception
# and the traceback. If it returns True, exception in with will be suppressed.
#
# Ex:
# with open('lesson33_context-manager.txt', 'w') as file:
#     ...
class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('OPENNING FILE')
        self._file = open(self.file_path, self.mode, encoding='utf8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('CLOSING FILE')
        self._file.close()

FILE_PATH = 'lesson33_context-manager.txt'

with MyOpen(FILE_PATH, 'w') as file: # the return of variable 'something' will the return of __enter__
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
    print('WITH', f'{file=}')