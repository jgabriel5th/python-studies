'''
Introduction to try/except
try -> try to execute the code.
except -> occurred some error by trying to execute.
'''
# int('a') # <- Exception
number = input("I'll double the number you type: ")
try:
    number_float = float(number)
    print(f'The double of {number} is {number_float * 2}')
except:
    print('This is not a number.')


# isdigit() - method used to see if a number is a integer.

# if number.isdigit():
#     number_float = float(number)
#     print(f'The double of {number} is {number_float * 2}')
# else:
#     print('This is not a number.')