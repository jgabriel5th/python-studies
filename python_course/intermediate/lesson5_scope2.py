'''
There are global and local scopes.
Global scope is the scope where the whole code is reachable.
Local scope is the where only names of the same local can be
reached.
We don't have access to names from inner scopes in outer scopes.
The global word make a variable from an outer scope the same in inner scope.
'''

x = 1

def scope():
    global x
    x = 10

    def other_function():
        global x
        x = 11
        y = 2
        print(x, y)

    other_function()
    print(x)

print(x)
scope()
print(x)