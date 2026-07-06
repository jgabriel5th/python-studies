'''
Precautions with mutable data
= - copied the value (immutable)
= - points to the same value in the memory (mutable)
'''
# Immutable data
name = 'Luiz'
another_variable = name # name was copied to another_variable
name = 'John'
print(name)
print(another_variable)

# Mutable data
list_a = ['Botafogo', 'Sulamericana']
list_b = list_a # Appointing to the same value in the memory.

list_a.append('Campeão')
list_a.append(2026)
print(list_b) # list_a was changed but list_b as well.

# How to solve(for now)
list_c = [1, 2, 3, 4, 5, 6]
list_d = list_c.copy() # This method will make a copy of list_c to list_d

list_c.append(True)
print(list_c) 
print(list_d) # Now they're different