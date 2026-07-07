'''
Tuple type - An immutable list
'''
# Ways of creating a tuple:
names = 'John', 'Locke', 'Watson' # That's a tuple
nombres = ('Albert', 'Einstein', 'Wick') # That's also a tuple but with ().

# Converting a list into a tuple:
list1 = [True, False, 1, 2, 3]
list1 = tuple(list1) # tuple() is used to convert a list into a tuple(or else).
print(list1)

# Converting a tuple into a list:
tuple1 = (1, 2, 3, 4, 5, 6, 7)
tuple1 = list(tuple1) # list() is used to convert a tuple into a list(or else).
print(tuple1)