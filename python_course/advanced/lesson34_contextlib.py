# Context Manager with function - Creating and Using context managers
from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('Opening file')
        file = open(file_path, mode, encoding='utf8')
        yield file
    except Exception as e:
        print('An error occurred', e)
    finally:
        print('Closing file')
        file.close()

with my_open('lesson34_contextlib.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n', 123)
    file.write('Line 3\n')
    print('WITH', file)