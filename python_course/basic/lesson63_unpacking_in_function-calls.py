# Unpacking in functions and methods calls
string = 'ABCD'
list1 = ['Mary', 'Agar', 1, 2, 3, 'Lou']
tuple1 = 'Python', 'is', 'nice'

# a, b, *_, c, d = list1 # It's possible to put the rest of the unpacking in the middle of it.
# print(a, d)

# for name in list1:
#     print(name, end=' ') # Output: Mary Agar 1 2 3 Lou %

# Best way to do it:
print(*list1) # It only works with iterables
print(*string)
print(*tuple1)