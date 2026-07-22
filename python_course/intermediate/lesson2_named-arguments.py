'''
Named and non-named arguments in Python functions.
Named argument(keyword) has a name with an equal sign "=".
Non-named argument(positional) receives only the argument(value).
'''

def Sum(x, y, z):
    # Definition
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z) # f'{x=} == x={x}'

Sum(1, 2, 3) # Non-named arguments(positional), they'll go according to the order.
Sum(z=3, y=2, x=1) # Named arguments, they receive the value with "=". They'll work regardless the order.
Sum(3, y=2, z=5) # Whenever a named argument is declared, it forces the subsequents arguments to be named as well.