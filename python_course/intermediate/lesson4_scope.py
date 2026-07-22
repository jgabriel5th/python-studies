'''
Scope of functions in Python.
Scope means the range where that code can reach.
There are global and local scope.
The global scope is the scope where all the code is reachable.
The local scope is the scope where only names of the same local can
be reached.
'''
x = 1 # module(archive/global) scope

def scope():
    # global x # with 'global' it's possible to change x(module) outside function scope.
    x = 10 # this variable x is different from variable x(module), because
    # is inside function scope.
    def other_function():
        # global x # though it's not recommended.
        x = 20 # now this x is different from x(scope()) and x(module)
        y = 2 # function scope. scope() doesn't have access to it.
        print(x, y) # this function has access to x because it's a variable from module scope.
    other_function() # A function can be executed(called) inside other.
    print(x)

print(x) # Output: 1
# print(x) # x was not defined.
scope()
print(x) # Output: 1