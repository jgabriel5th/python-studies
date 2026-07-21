'''
Introduction to functions (def) in Python:
Functions are code snippets used to replicate an action
throughout your code. They can receive values for parameters (arguments)
and return an especific value.
As standard, Python functions return None.
'''

def printName(a, b ,c): # Parameters("variables")
    print(a, b, c)

printName('John', 2, True) # Arguments(values)
printName('Gabriel', 3, False) # Arguments(values)


def greeting(name='person'): # name='No name' it serves to put a standard value in case a function is called
# Without an argument.
    print(f'Hello, {name}!')

greeting('Newton')
greeting('Louise')
greeting('World')
greeting()
