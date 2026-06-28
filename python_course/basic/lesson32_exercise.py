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
Make a program that asks the hour to the user and based by the hour described,
print the appropriated greeting. Ex.: Good morning 0-11, Good afternoon 12-17 and
Good evening 18-23. <- Brazil time zone
'''
try:
    time = input('Type the current hour(24-hour format): ')
    time = int(time)
    good_morning = time <= 11 # using AND operator: time >= 0 and time <= 11
    good_afternoon = time == 12 or time <= 17 # using AND operator: time >= 12 and time <= 17
    good_evening = time == 18 or time <= 23 # using AND operator: time >= 18 and time <= 23

    if good_morning:
        print('Good morning!')
    elif good_afternoon:
        print('Good afternoon!')
    elif good_evening:
        print('Good evening!')
    else:
        print("I don't know this hour")
except:
    print('Invalid value, type again')

'''
Make a program that asks the first user's name. If the name has 4 letters or less
write "Your name is short"; if the name has 5 and 6 letters, write "Your name is normal";
greater than 6 write "Your name is name very long".
'''
first_name = input("Type your first name: ")
short_name = len(first_name) > 1 and len(first_name) <= 4
normal_name = len(first_name) == 5 or len(first_name) == 6
long_name = len(first_name) > 6


if short_name:
    print('Your name is short')
elif normal_name:
    print('Your name is normal')
elif long_name:
    print('Your name is very long')
else:
    print('Invalid value, type again')