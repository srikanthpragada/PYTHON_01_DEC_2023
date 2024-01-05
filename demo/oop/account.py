class FundsError(Exception):
    def __init__(self, balance, amount):
        self.msg = f"Insufficient balance {balance} for amount {amount}"

    def __str__(self):
        return self.msg


class SavingsAccount:
    minbal = 10000

    @staticmethod
    def setminbal(newminbal):
        SavingsAccount.minbal = newminbal

    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            raise FundsError(self.balance - SavingsAccount.minbal, amount)

    def getbalance(self):
        return self.balance

    def show(self):
        print(self.acno, self.ahname, self.balance)

    @property
    def currentbalance(self):
        return self.balance


s1 = SavingsAccount(1, "Mark", 50000)
s2 = SavingsAccount(2, "Scott")

s1.deposit(10000)
try:
    s1.withdraw(55000)
except FundsError as ex:
    print(ex)

print(s1.currentbalance)  # access a property
