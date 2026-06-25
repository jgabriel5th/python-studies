# Logical operators
# AND, OR, NOT

# OR - Any true condition makes the whole expression true.
# If any value is considered true, the entire expression will be evaluated as true.
# Values considered false: 0, 0.0, '', False # There are others
# It also exists the type None that is used to represent a non-value.

# Unreal example:
entrance = input('[E]nter [Q]uit: ')
password_typed = input('Password: ')

permitted_password = '123456'
# if True:
#   ...
if (entrance == 'E' or entrance == 'e') and password_typed == permitted_password:
    print('Enter')
else:
    print('Quit')

# Short-circuit evaluation
print(True or False) # Output: True
print(0 or False or 0 or 'abc' or True) # Output: 'abc'; Reason: Python stops on the first True('abc') value.
password = input('Password: ') or 'No password'
print(password)