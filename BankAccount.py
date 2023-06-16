class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__()
        self.interest_rate = interest_rate

    def get_balance(self):
        balance = super().get_balance()
        return balance + (balance * self.interest_rate)

class CheckingAccount(BankAccount):
    def __init__(self, transaction_fee):
        super().__init__()
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        super().withdraw(amount)
        self.balance -= self.transaction_fee

# Create instances of SavingsAccount and CheckingAccount
savings_account = SavingsAccount(interest_rate=0.05)
checking_account = CheckingAccount(transaction_fee=1.5)

# Perform operations
savings_account.deposit(1000)
checking_account.deposit(500)
savings_account.withdraw(200)
checking_account.withdraw(100)

# Print balances
print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())
