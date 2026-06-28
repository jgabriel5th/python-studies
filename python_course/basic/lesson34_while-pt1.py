'''
Repetitions
while - It executes an action while a condition is True.
Endless loop -> When a code doesn't have an end.
'''
condition = True

# while condition: # <- Example of endless loop
#     print(1)
#     print(2)
#     print(3)

while condition:
    name = input('What is your name: ')
    print(f'Your name is {name}')

    if name:
        print("That's a good name")
        break

print('The loop has finally ended')