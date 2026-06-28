'''
https://docs.python.org/pt-br/3/library/stdtypes.html <- Python documentation.
Built-in types: types that exist in Python language natively.
Immutables already seen: str, int, float, bool <- all these types are objects which means they have methods such as isdigit() for str.
'''
string = 'John Watson'
another_variable = string # another_variable is copying the value from variable string.
try:
    string[3] = 'ABC' # it'll raise an exception, because type str is immutable
    print(string[3])
except:
    print('Type str is immutable')

another_variable = f'{string[:3]}ABC{string[4:]}' # Different value
print(another_variable.zfill(20))