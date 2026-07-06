'''
Lists in Python
List type - Mutable
It supports several values of any type;
Reusable knowledge - index and slicing;
Usable methods: append, insert, pop, del, clear, extend, +
'''
#         01234
#        -54321
string = 'ABCDE' # 5 characters
# list1 = list() # type conversion
list2 = [123, True, 'John', 1.2, []]
# print(bool([])) # Output: False; because it's an empty list.
# print(type(list2)) # Output: <class 'list'>

#        0    1      2      3    4
#       -5   -4     -3     -2   -1
list2 = [123, True, 'John', 1.2, []]

list2[-3] = 'Brazil' # Changing a value
print(list2[2].upper(), type(list2[2])) # Using a method