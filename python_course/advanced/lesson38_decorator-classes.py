# Decorator classes
class Multiply:
    def __init__(self, multiplier):
        self._multiplier = multiplier

    @property
    def multiplier(self):
        return self._multiplier

    def __call__(self, func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self.multiplier
        return inner

@Multiply(10)
def sumNumber(x, y):
    return x * y

two_plus_two = sumNumber(2, 2)
print(two_plus_two)