# Reusing the code from cpf-validator repository
import random
import sys
for _ in range(10):
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))

    typed_cpf = cpf[:9]

    countdown = 10
    result = 0
    for number in typed_cpf:
        result += int(number) * countdown
        countdown -= 1

    final_result = (result * 10) % 11
    first_digit = 0 if final_result > 9 else final_result


    typed_cpf = f'{cpf[:9]}{first_digit}'
    countdown2 = 11
    result2 = 0
    for number2 in typed_cpf:
        result2 += int(number2) * countdown2
        countdown2 -= 1

    final_result2 = (result2 * 10) % 11
    second_digit = 0 if final_result2 > 9 else final_result2
    typed_cpf = f'{cpf[:9]}{first_digit}{second_digit}'
    print(f'Random CPF gerated: {typed_cpf}')                                    