# Create a Bank ATM Simulation using:, User Authentication, Deposit, Withdraw, Transfer, Show mini statement
class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount}")

    def transfer(self, amount, recipient_atm):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        recipient_atm.deposit(amount)
        self.transaction_history.append(f"Transferred: ${amount} to recipient")

    def mini_statement(self):
        return self.transaction_history[-5:]


my_atm = ATM(1000)
my_atm.deposit(500)
my_atm.withdraw(200)
print(my_atm.mini_statement())
my_atm2 = ATM(500)
my_atm.transfer(300, my_atm2)
print(my_atm2.balance)
print(my_atm.mini_statement())
