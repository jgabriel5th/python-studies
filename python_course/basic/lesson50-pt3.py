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
#        0   1   2   3   4
list1 = [10, 20, 30, 40, 50]
#       -5  -4  -3  -2  -1
list_example = [1, 2, 3, 4, 5, 6, 7]
list1.append('Botafogo')
name = list1.pop()
print(name, type(name))
list1.append(12345)
del list1[-1]
list_example.clear()
list1.insert(0, True) # This method receives two arguments: the index and the value.
list1.insert(100, False) # Index 100 doesn't exist in this list, but Python will consider the last existing index.
print(list1, list_example)