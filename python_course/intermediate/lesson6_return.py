'''
Return of values in functions(return)
'''

def sumNumbers(x, y):
    print(x + y)


# variable = print('John')
# variable = None
# variable = sumNumbers(1, 2) # Output: 3 None
# variable = int('1') # It returns a value
try:
    sum1 = sumNumbers(2, 4)
    sum2 = sumNumbers(2, 2)
    print(sum1 + sum2) # It'll raise a TypeError because of a NoneType.
except TypeError:
    print('It does not work')

# How to solve:

def sumNumbers2(x, y):
    if x > 10:
        return [10, 20] # It returns only a value(list).
    return x + y # It's put in the end.
    print(1, 2, 3) # It won't be executed, just things before return.

sum3 = sumNumbers2(2, 4)
sum4 = sumNumbers2(2, 2)
print(sumNumbers2(11, 22))
print(f'{sum3} + {sum4} = {sum3 + sum4}')