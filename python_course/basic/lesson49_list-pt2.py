'''
Lists in Python
List type - Mutable
It supports several values of any type;
Reusable knowledge - index and slicing;
Usable methods: 
    append, insert, pop, del, clear, extend, +
Create, Read, Update, Delete = list[i] (CRUD)
'''
#        0   1   2   3   4
list1 = [10, 20, 30, 40, 50]
# list1[2] = 300
# del list1[2] # method used to delete a chosen list index.
# print(list1)
# print(list1[2])
list1.append(60) # method used to append a value in the end of the list.
list1.pop() # method used to remove the last element in the list and returns an int value. In this case: 60
list1.append(70)
list1.append(80)
last_value = list1.pop(3) # pop() also can be used to remove a chosen element by its index.
print(list1, 'Removed:', last_value)

'''
For lists with a large amount of elements, it's not recommended to remove an element
in the middle of it. According to the course's teacher, the remotion of an element would
make the moving of the others and consequently make the program run slowly, so big lists should be used to append
elements and remove elements in the end of them.
'''