'''
Ask the user to type their name;
Ask the user to type their age;
If the name and age are typed:
    print:
        Your name is {name}
        Your name inverted is {inverted name}
        Your name has(or not) spaces
        Your name has {n} letters
        The first letter of your name is {letter}
        The last letter of your name is {letter}
If anything is typed in name or age:
    print "Sorry, you left empty spaces."
'''
name = input("Type your name: ")
age = input("Type your age: ")
age = int(age)

if name and age:
    print(f'Your name is {name}')
    print(f'Your name inverted is {name[::-1]}')
    if ' ' in name:
        print('Your name has spaces')
    else:
        print("Your name doesn't have spaces")
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is {name[0]}')
    print(f'The last letter of your name is {name[-1]}')
else:
    print('Sorry, you left empty spaces.')