# Precedence of arithmetic operators:
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
operation_1 = 1 + 1 ** 5 + 5 # 7
operation_2 = (1 + 1) ** (5 + 5) # 1024
operation_3 = (1 + int((0.5 + 0.5))) ** (5 + 5) # 1024
print(operation_1)
print(operation_2)
print(operation_3)