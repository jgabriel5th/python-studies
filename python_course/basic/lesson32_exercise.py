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

