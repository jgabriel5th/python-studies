'''
Flag - Used to mark a place.
None = non-value.
Is and is not = confirm identification of a value(type, value, identity)
id = Identity
'''

# v1 = 'a'
# v2 = 'a'
# print(id(v1)) # id() it serves to see the identity of an element in the computer memory.
# print(id(v2)) # The two variables have the same id in Python, but it can be changed.
# v2 = 'b'
# print(id(v2))

condition = True
passed_in_if = None

if condition:
    passed_in_if = True # Flag. Obs.: It's not recommended to define variable inside if-structure, usually it's better to define variables outside it.
    print('Do something')
else:
    print("Don't do anything")

print(passed_in_if, passed_in_if is None) # <- None is followed by is or is not instead of ==
print(passed_in_if, passed_in_if is not None)

if passed_in_if is None:
    print('Not passed in if')
else:
    print('Passed in if')