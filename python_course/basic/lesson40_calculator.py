'''Calculator with while-structure'''
result = 0
while True:
    number1 = input('Type a number: ')
    number2 = input('Type another number: ')
    operator = input('Choose the math operation(sum/sub/multi/division): ')
    if operator == 'sum':
        number1 = int(number1)
        number2 = int(number2)
        result = number1 + number2
        print(f'The result of your sum is {result}')

    if operator == 'sub':
        number1 = int(number1)
        number2 = int(number2)
        result = number1 - number2
        print(f'The result of your subtraction is {result}')

    if operator == 'multi':
        number1 = int(number1)
        number2 = int(number2)
        result = number1 * number2
        print(f'The result of your multiplication is {result}')
    
    if operator == 'division':
        number1 = int(number1)
        number2 = int(number2)
        result = number1 // number2
        print(f'The result of the division is {result}')

    question = input('Would you like to continue to calculate?(Y/N): ')
    if question == 'Y' or question == 'y':
        continue
    elif question == 'N' or question == 'n':
        print('Thanks for using the calculator!')
        break
    else:
        print('You typed an invalid value')

print('The final result of your operation is', result)