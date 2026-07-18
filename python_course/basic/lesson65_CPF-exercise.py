'''
Calculation of the first digit - CPF
CPF: 746.824.890-70
Collect the sum from the first 9 digits of the CPF multiplying each
one of the values by a countdown starting from 10.

Ex.: 746.824.890-70 (746824890)
    10  9   8   7   6   5   4   3   2
*   7   4   6   8   2   4   8   9   0
    70  36  48  56  12  20  32  27  0

Sum all the results:
70+36+48+56+12+20+32+27+0 = 301

Multiply the previous result by 10:
301 * 10 = 3010

Obtain the rest of the division from the previous result by 11:
3010 % 11 = 7

If the previous result is bigger than 9:
    result is 0
else:
    result is calculation result

The first digit of the CPF is 7
'''
cpf_list = []
while len(cpf_list) < 9:
    cpf = input('Type the first 9 digits of a CPF(One number at a time): ')
    if len(cpf) == 1:
        int_cpf = int(cpf)
        cpf_list.append(int_cpf)
        print(*cpf_list)
    else:
        print('Only one number at a time is permitted')

countdown = 10
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
first_digit = 0 if calculation_result > 9 else calculation_result
print(f'The first digit of the CPF is {first_digit}')