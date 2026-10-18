import math
class ProtectedAccount:
    def __init__(self, name: str, age: int, bank: str):
        self._validate(name, age, bank)
        self.name = name
        self.age = age
        self.bank = bank
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @staticmethod
    def _validate(name, age, bank):
        if any(not isinstance(value, str) for value in (name, bank)):
            raise TypeError('Value must be string')
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError('Age must be integer')
        if any(not value.strip() for value in (name, bank)):
            raise ValueError('Empty value not allowed')
        if age < 0 or not math.isfinite(age):
            raise ValueError('Negative/infinite number not allowed')

    def deposit(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
             print('Non number informed. Operation aborted...')
        elif value <= 0 or not math.isfinite(value):
            print('Negative/infinite number informed. Operation aborted...')
        else:
            self._balance += value

    def withdrawal(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            print('Non number informed. Operation aborted...')
        elif value <= 0 or not math.isfinite(value):
            print('Negative/infinite number informed. Operation aborted...')
        elif value > self.balance:
            print('Not enough value in balance. Operation aborted...')
        else:
            self._balance -= value

    def show_balance(self):
        return self.balance

    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

p1 = ProtectedAccount('Johnny', 90, 'Imaginary bank')
p1.deposit(1000)
p1.withdrawal(900)
print(p1.show_balance())