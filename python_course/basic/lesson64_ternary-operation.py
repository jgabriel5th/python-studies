'''
Ternary operation (conditional in a single line)
<value> if <condition> else <other value>
print('Value' if True else 'Other value')
'''
# Example:
# condition = 10 == 10
# variable = 'Value' if condition else 'Other value'
# print(variable)

# CPF - Digit:
digit = 9 # > 9 = 0
new_digit = digit if digit <= 9 else 0
new_digit = 0 if digit > 9 else digit
print(new_digit)

print('Value' if False else 'Other value' if False else 'End') # Not recommended though possible.