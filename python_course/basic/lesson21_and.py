# Logical operators
# AND, OR, NOT

# AND - All the conditions must be true.
# If any value is considered false, than the whole expression is false as well.
# Values considered false: 0, 0.0, '', False # There are others
# It also exists the type None that is used to represent a non-value.

# Unreal example:
entrance = input('[E]nter [Q]uit: ')
password_typed = input('Password: ')

permitted_password = '123456'
# if True:
#   ...
if entrance == 'E' and password_typed == permitted_password: # If anything is false, Python skips the whole if-structure, going straight to else-structure.
    print('Enter')
else:
    print('Quit')

# Short-circuit evaluation
print(True and False and True)
