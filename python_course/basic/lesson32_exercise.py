'''
Make a program that asks the user to type an integer number, inform if
this number is even or odd. In case the user doesn't type an integer number,
inform that it isn't an integer number.
'''
try:
    number = input('Type a number: ')
    number = int(number)
    evenNumber = number % 2 == 0
    if evenNumber:
        print("This is an even number")
    else:
        print("This is an odd number")
except:
    print('This is not an integer number')

'''
Make a program that asks the time to the user and based by the time described,
print the appropriated greeting. Ex.: Good morning 0-11, Good afternoon 12-17 and
Good evening 18-23. <- Brazil time zone
'''
try:
    time = input('Type the current time(24-hour format): ')
    time = int(time)
    good_morning = time <= 11
    good_afternoon = time == 12 or time <= 17
    good_evening = time == 18 or time <= 23

    if good_morning:
        print('Good morning!')
    elif good_afternoon:
        print('Good afternoon!')
    elif good_evening:
        print('Good evening!')
    else:
        print('You typed an invalid value')
except:
    print('Invalid value, type again')