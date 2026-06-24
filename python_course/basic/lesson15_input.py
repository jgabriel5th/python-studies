# name = input("What's your name? ") # <- str - Function used to collect user's data
# print(f'Your name is {name=}') # By putting name= it'll print the variable and its value(optional).

number1 = input('Type a number: ')
number2 = input('Type another number: ')
# number1 = int(input('Type a number: ')) <- Typecasting
# number2 = int(input('Type another number: '))

int_number1 = int(number1)
int_number2 = int(number2)

print(f'The sum of the numbers is: {int_number1 + int_number2}')