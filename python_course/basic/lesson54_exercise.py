'''
Exercise
Print the list index
0 Football
1 Basketball
2 Volleyball
'''
# The way I used:
list1 = ['Football', 'Basketball', 'Volleyball']
list1.append('Baseball')

number = 0
for name in list1:
    print(number, name)
    number += 1

# The other way:
list2 = ['Judo', 'Boxe', 'Taekwondo']
list2.append('Muay Thai')

indices = range(len(list2))

for index in indices:
    print(index, list2[index], type(list2[index]))