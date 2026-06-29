'''
Repetitions
while - It executes an action while a condition is True.
break - stops a while-loop when a condition inside it is done.
Endless loop -> When a code doesn't have an end.
continue - ignores something inside a while-structure.
'''
counter = 0

while counter < 100:
    counter += 1
    if counter == 6:
        print("I'm not going to show 6.")
        continue
    if counter >= 10 and counter <= 15: # It ignores 10, 11, 12, 13, 14, 15
        continue
    print(counter)
    if counter == 40:
        break

print('Over')