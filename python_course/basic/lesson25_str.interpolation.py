'''
Basic string interpolation
s - string
d and i - int
f - float
x and X - Hexadecimal(0123456789ABCDEF)
'''
name = 'John'
price = 1548.39842202
variable = '%s, the price is R$%.2f' % (name, price) # Quite similar to format(), but it needs "%" before the variable.
print(variable)
print('The hexadecimal of %d is %x' % (15, 15))