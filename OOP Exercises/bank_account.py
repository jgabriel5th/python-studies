class BankAccount:
    def __init__(self, name: str, age: int, agency: int, account_number: int):
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
    def _validate(name, age, agency, account_number):
        if not isinstance(name, str):
            raise TypeError('Name must be string')
        if not name.strip():
            raise ValueError('Name cannot be empty')
        
        if any(not isinstance(value, int) or isinstance(value, bool) for value in (age, agency, account_number)):
            raise TypeError('Value must be integer')
        
        if any(value < 0 for value in (age, agency, account_number)):
            raise ValueError('Negative numbers not allowed')
        
        
    def deposit(self, value):
        if isinstance(value, (float, int)) and value > 0:
            self._balance += value
            return "Operation concluded"
            
        return 'Informed value is not valid. Operation aborted...'
        
    def info_balance(self):
        return f'Balance: ${self._balance}'
    
    def withdrawal(self, value):
        if self._balance == 0:
            return f'Your balance is {self._balance}, it is not possible to withdrawal'
            
        if isinstance(value, (float, int)) and value <= self._balance and value > 0:
            self._balance -= value
            return "Operation concluded"

        return 'Value higher than available in balance or invalide value. Operation aborted...'

account1 = BankAccount('John', 2039, 2050, 2084)