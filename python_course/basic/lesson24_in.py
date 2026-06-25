# Operators in and not in
# Strings are iterables
#  0 1 2 3 4 5
#  J o h n n y
# -6-5-4-3-2-1
name = 'Johnny'
# print(name[2])
# print(name[-4])
print('John' in name) # True
print('eight' in name) # False
print('eight' not in name) # True

# Small example:
name_user = input('Type your name: ')
find = input('Type what you wish to find: ')

if find in name_user:
    print(f'{find} has in {name_user}')
else:
    print(f"{find} doesn't have in {name_user}")

print(name, name)