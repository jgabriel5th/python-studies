import math
class BankAccount:
    def __init__(self, name: str, age: int, agency: str, account_number: str):
        self._validate(name, age, agency, account_number)
        self.name = name
        self.age = age
        self.agency = agency
        self.account_number = account_number
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance

    @staticmethod
    def _validate(name: str, age: int, agency: str, account_number: str):
        if any(not isinstance(value, str) for value in (name, agency, account_number)):
            raise TypeError('Value must be string')
        
        if not name.strip():
            raise ValueError('Name cannot be empty')
        
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError('Age must be integer')
        
        if age < 0:
            raise ValueError('Negative numbers not allowed')

        if not all(value.isdigit() for value in (agency, account_number)):
            raise ValueError('Negative numbers are not allowed')
            
        
        
    def deposit(self, value):
        if isinstance(value, (float, int)) and value > 0:
            if not math.isfinite(value) or isinstance(value, bool):
                return 'Invalid value. Operation aborted...'
            
            self._balance += value
            return "Operation concluded"
            
        return 'Informed value is not valid. Operation aborted...'
        
    def info_balance(self):
        return f'Balance: ${self._balance}'
    
    def withdrawal(self, value):
        if isinstance(value, (float, int)) and value > 0 and value <= self._balance:
            if not math.isfinite(value) or isinstance(value, bool):
                return 'Invalid value. Operation aborted...'
            
            self._balance -= value
            return "Operation concluded"
            

        return 'Value higher than available in balance or invalid value. Operation aborted...'

account1 = BankAccount('John', 2039, "2050", "2084")
print(account1.name)
print(account1.deposit(float('inf')))
print(account1.deposit(True))
print(account1.deposit(1000))
print(account1.info_balance())
print(account1.withdrawal(True))
print(account1.info_balance())
