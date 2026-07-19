'''
Calculation of the second digit - CPF
CPF: 746.824.890-70
Collect the sum from the first 9 digits of the CPF,
PLUS THE FIRST DIGIT,
multiplying each one of the values by a countdown starting from 11.

Ex.: 746.824.890-70 (746824890)
    11  10  9   8   7   6   5   4   3   2
    7   4   6   8   2   4   8   9   0   7 < - - FIRST DIGIT
    77  40  54  64  14  24  40  36  0   14

Sum all the results:
77+40+54+64+14+24+40+36+0+14 = 363

Multiply the previous result by 10:
363 * 10 = 3630

Obtain the rest of the division from the previous calculation by 11:
3630 % 11 = 0

if the previous result is bigger than 9:
    result is 0
else:
    result is calculation result

The second digit of the CPF is 0
'''
cpf_list = []
while len(cpf_list) < 10:
    cpf = input('Type the 10 digits of a CPF(One number at a time): ')
    if len(cpf) == 1:
        int_cpf = int(cpf)
        cpf_list.append(int_cpf)
        print(*cpf_list)
    else:
        print('Only one number at a time is permitted')

countdown = 11
results = []

for number in cpf_list:
    result = number * countdown
    results.append(result)
    countdown -= 1

number2 = 0
for number1 in results:
    number2 += number1
    sum_result = number2

calculation_result = (sum_result * 10) % 11
second_digit = 0 if calculation_result > 9 else calculation_result
print(f'The second digit of the CPF is {second_digit}')