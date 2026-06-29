'''
Repetitions
while - It executes an action while a condition is True.
break - stops a while-loop when a condition inside it is done.
Endless loop -> When a code doesn't have an end.
continue - ignores something inside a while-structure.
'''
amount_lines = 5
amount_columns = 5

line = 1
while line <= amount_lines:
    column = 1
    while column <= amount_columns: # while inside another, similar to a small gear inside a large gear.
        print(f'{line=} {column=}')
        column += 1
    line += 1

print('Over')