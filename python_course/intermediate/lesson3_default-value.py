'''
Default values for parameters.
When defining a function, the parameters can have default values.
In case the value doesn't be sent to the parameters, the default value
will be used instead.
Refactor: edit the code.
'''

# def sumNumbers(x, y, z=0): # 0 == False;
#     if z:
#         print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)
#     else:
#         print(f'{x=} {y=}', '|', 'x + y =', x + y)

# Best way: 
def sumNumbers(x, y=1, z=None): # As it happens with named arguments. Whenever a named parameter is defined
    # the subsequents parameters need to be named as well.
    if z is not None:
        print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)
    else:
        print(f'{x=} {y=}', '|', 'x + y =', x + y)
        
sumNumbers(1, 2)
sumNumbers(3, 4)
sumNumbers(6, 8, 0)
sumNumbers(z=6, x=8, y=0)