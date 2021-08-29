class BankAccount():

    def __init__(self, name):
        self.name = name
        self.balance = 0.00

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            return
        if amount > self.balance:
            return
        self.balance = self.balance - amount