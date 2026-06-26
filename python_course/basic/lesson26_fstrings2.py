'''
Basic string formatting
s - string
d - int
f - float
.<number of digits>f
x or X - Hexadecimal
(Caractere)(><^)(quantity)
> - Left
< - Right
^ - Center
= - It forces the number to show before the zero.
Signal - + or -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variable = 'XYZ'
print(f'{variable}')
print(f'{variable: >10}')
print(f'{variable: <10}')
print(f'{variable:#^10}')
print(f'{123498.094380:0=+20,.2f}')
print(f'The hexadecimal of 1500 is {1500:08x}')