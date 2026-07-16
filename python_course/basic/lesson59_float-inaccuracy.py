'''
Floating-point inaccuracy
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
'''
import decimal

number1 = 0.1
number2 = 0.7
number3 = number1 + number2
print(number3)
print(f'{number3:.2f}') # Solution 1
print(round(number3, 1)) # Solution 2: it returns a float type
number4 = decimal.Decimal('0.2') # Solution 3
number5 = decimal.Decimal('0.8')
number6 = number4 + number5
print(number6)