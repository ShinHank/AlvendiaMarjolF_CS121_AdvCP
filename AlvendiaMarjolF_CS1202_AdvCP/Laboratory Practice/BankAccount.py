from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, account_number, balance = 0.0):
        self.__account_number = account_number
        self.__balance = balance
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    def _set_balance(self, amount):
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def display_account_type(self):
        pass

class CurrentAccount(BankAccount):

    def deposit(self, amount):
        self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        if self.balance - amount >= -5000:
            self._set_balance(self.balance - amount)
    
    def display_account_type(self):
        return "Current Account"


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self._set_balance(self.balance - amount)
        
    def display_account_type(self):
        return "Savings Account"
    
def acc_detail(account):
    print(f"Account Number: {account.account_number}")
    print(f"Account Number: {account.balance}")
    print(f"Account Number: {account.display_account_type()}")
    print("-" * 30)

A1 = SavingsAccount('SA123', 5000)
A2 = CurrentAccount('CA456', 5000)
A1.deposit(1000)
A2.withdraw(8000)
accounts = [A1, A2]

for i in accounts:
    acc_detail(i)
    
