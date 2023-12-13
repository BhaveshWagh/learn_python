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
            print(f"${amount} This withdrawal will not be allowed due to insufficient funds")
        self.balance -= amount

account = BankAccount("John Doe")
print(f"Initial balance: ${account.balance}")

account.deposit(100.00)
print(f"Balance after deposit: ${account.balance}")

account.withdraw(50.00)
print(f"Balance after withdrawal: ${account.balance}")

account.withdraw(80.00)  # This withdrawal will not be allowed due to insufficient funds
print(f"Balance after attempted withdrawal: ${account.balance}")

