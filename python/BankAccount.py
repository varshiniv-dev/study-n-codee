#Create a class BankAccount with: deposit(), withdraw(), check_balance() methods. Initialize balance through constructor . Perform operations for multiple users
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def check_balance(self):
        return self.balance


account1 = BankAccount(100)
account1.deposit(50)
account1.withdraw(30)
print("Account 1 Balance:", account1.check_balance())
account2 = BankAccount(200)
account2.deposit(100)
account2.withdraw(150)
print("Account 2 Balance:", account2.check_balance())
