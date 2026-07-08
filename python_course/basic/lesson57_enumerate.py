'''
enumerate - enumerate iteratables (indices)
'''
list1 = ['John', 'Mary', 'Sophia']
list1.append('Gabriel')

enumerated_list = enumerate(list1)
print(enumerated_list) # Iterator

for item in enumerated_list:
    print(item) # it creates a tuple for every for-loop

for item in enumerated_list: # It won't come nothing in output, because the iterator was used previously.
    print(item)

for item in enumerate(list1): # That's a way to solve the problem above.
    print(item)

# How to print enumerate()
list2 = [1, 2, 3, 4, 5, 6]

enumerated_list2 = list(enumerate(list2)) # Type conversion
print(enumerated_list2) # Now the Output won't be the iterator.

# How to avoid tuples in for with enumerate(): first way
for item in enumerate(list1):
    index, name = item # Unpacking
    print(index, name)

# How to avoid tuples in for with enumerate(): second way
for index, name in enumerate(list1): # Unpacking since the beginning the for
    print(index, name)

# How to use tuple with enumerate():
for enumerated_tuple in enumerate(list1):
    print('Tuple FOR:')
    for value in enumerated_tuple:
        print(f'\t{value}') # \t it's like tab key.