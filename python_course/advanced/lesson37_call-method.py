# Special method __call__
# Callable is something which can be executed with parentheses
# In normal classes, __call__ make the class's instance "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(name, 'is calling', self.phone)
        # return 1234 # It's possible to put a return as well

call1 = CallMe('1234567890')
return1 = call1('John')
print(return1)
