'''
Lists in Python
List type - Mutable
It supports several values of any type;
Reusable knowledge - index and slicing;
Usable methods: 
    append - Adds an element in the end.
    insert - Adds an elements in the chosen index.
    pop - Removes in the end or in the chosen index and returns the value.
    del - Deletes an index.
    clear - Clears the list.
    extend - Extends the list.
    + - Concatenate lists.
Create, Read, Update, Delete = list[i] (CRUD)
'''
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
list_a.extend(list_b) # It changes directly list_a by extending it with list_b. It's important to note that extend() return None
# so it cannot be assigned to any variable.
print(list_c)
print(list_a)