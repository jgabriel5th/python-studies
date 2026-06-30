'''Calculator with while-structure'''
while True:
    try:
        number1 = input('Type a number: ')
        number2 = input('Type another number: ')
        operator = input('Choose the math operation(sum/sub/multi/division): ').lower()
        sumSelection = operator == 'sum'
        subSelection = operator == 'sub'
        multiSelection = operator == 'multi'
        divisionSelection = operator == 'division'

        if sumSelection:
            number1 = int(number1)
            number2 = int(number2)
            result = number1 + number2
            print(f'The result of your sum is {number1} + {number2} = {result}')

        elif subSelection:
            number1 = int(number1)
            number2 = int(number2)
            result = number1 - number2
            print(f'The result of your subtraction is {number1} - {number2} = {result}')

        elif multiSelection:
            number1 = int(number1)
            number2 = int(number2)
            result = number1 * number2
            print(f'The result of your multiplication is {number1} * {number2} = {result}')
        
        elif divisionSelection:
            number1 = int(number1)
            number2 = int(number2)
            result = number1 // number2
            print(f'The result of the division is {number1} / {number2} = {result}')

        question = input('Would you like to continue to calculate?(y/n): ').lower()
        yesQuestion = question == 'y'
        noQuestion = question == 'n'
        if yesQuestion:
            continue
        elif noQuestion:
            break
        else:
            print('You typed an invalid value')
    except:
        print('You typed an invalid value, try again')

print('Thanks for using the calculator!')