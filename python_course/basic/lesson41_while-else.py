'''while/else'''
string = 'Any value'

i = 0
while i < len(string):
    letter = string[i]

    if letter == ' ':
        print('Empty space found')
        break # When break is executed, else is not executed.

    print(letter)
    i += 1
else: # It's executed when the while-loop is completed and the value 'i' is False.
    print('It was not find an empty space')
print('Out of while')
