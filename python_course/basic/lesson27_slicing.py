'''
String slicing
012345678
Hello world
-987654321
Slicing [start:stop:step] [::]
Obs.: function len() returns the quantity of caracteres from the string.
'''
variable = 'Hello world'
print(variable[6:11]) # Output: world; Obs.: The last chosen index: will be excluded, that's why 6:11, instead 6:10.
print(variable[6:]) # Output: world; because it will from index 6 to the end.
print(variable[-5:]) # Output: world
print(variable[0:11:2]) # Step
print(variable[::-1]) # It'll invert the value inside the String.
print(len(variable)) # 11 caracteres