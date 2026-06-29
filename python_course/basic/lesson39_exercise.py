'''
Iterating strings with while
'''
#       012345678910
name = 'John Watson' # Iterables
#     1110987654321-
length_name = len(name)
print(name)
print(length_name)

index = 0
new_name = ''

while index < length_name:
    letter = name[index]
    new_name += f'*{letter}'
    index += 1

print(new_name)
    
# how to print String index in a while-structure - Practing
name_example = 'Lewandowski' 

length_nameExample = len(name_example)
index_example = 0

while index_example < length_nameExample:
    print(name_example[index_example])
    index_example += 1

print('Done')