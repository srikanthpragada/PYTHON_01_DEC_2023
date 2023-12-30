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
            print('Insufficient Funds')

    def getbalance(self):
        return self.balance

    def show(self):
        print(self.acno, self.ahname, self.balance)


s1 = SavingsAccount(1, "Mark", 50000)
s2 = SavingsAccount(2, "Scott")

s1.deposit(10000)
s1.withdraw(55000)
print(s1.getbalance())
