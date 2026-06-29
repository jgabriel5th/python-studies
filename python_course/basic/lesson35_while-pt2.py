'''
Repetitions
while - It executes an action while a condition is True.
break - stops a while-loop when a condition inside it is done.
Endless loop -> When a code doesn't have an end.
'''
counter = 0
counter1 = 0

while counter < 10:
    counter = counter + 1
    print(counter) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

while counter1 <= 10:
    print(counter1) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    counter1 = counter1 + 1
    
print('Over')