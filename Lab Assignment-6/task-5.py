# bank_account.py
# Program to demonstrate a BankAccount class with deposit, withdraw, and balance methods

class BankAccount:
    """
    A simple class to represent a bank account.
    It supports depositing money, withdrawing money, and checking the balance.
    """

    def __init__(self, account_holder, initial_balance=0.0):
        """
        Constructor method to initialize account details.
        :param account_holder: str - Name of the account holder
        :param initial_balance: float - Initial amount in the account
        """
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"Account created for {self.account_holder} with balance ₹{self.balance:.2f}")

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        :param amount: float - Amount to deposit
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        :param amount: float - Amount to withdraw
        """
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f}. Remaining balance: ₹{self.balance:.2f}")

    def get_balance(self):
        """
        Method to return the current account balance.
        :return: float - Current balance
        """
        print(f"Current balance for {self.account_holder}: ₹{self.balance:.2f}")
        return self.balance


# ----------------------------
# Example Usage (Main Program)
# ----------------------------
def main():
    print("=== Welcome to Simple Bank Account Program ===\n")

    # Create an account with an initial balance
    account = BankAccount("Alice", 1000.0)

    # Perform deposit and withdrawal operations
    account.deposit(500.0)
    account.withdraw(200.0)
    account.get_balance()

    # Trying invalid transactions
    account.deposit(-100.0)
    account.withdraw(2000.0)


if __name__ == "__main__":
    main()
