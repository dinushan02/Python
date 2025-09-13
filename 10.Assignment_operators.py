"""a = 125
print(a)  # 125

a += 5  # a = a + 5
print(a)  # 130

a -= 10  # a = a - 10
print(a)  # 120

a *= 10  # a = a * 10
print(a)  # 1200

a /= 10  # a = a / 10
print(a)  # 120.0 (division always returns a float)

a %= 10  # a = a % 10
print(a)  # 0.0 (120.0 % 10 is 0.0)

a **= 10  # a = a ** 10
print(a)  # 0.0 (0.0 raised to any power is 0.0)

a //= 10  # a = a // 10
print(a)  # 0.0 (integer division of 0.0 by 10 is still 0.0)"""

#Project: Bank Account Balance Tracker
#This program allows users to deposit, withdraw, apply interest, and check their balance
#while utilizing assignment operators (+=, -=, *=, /=, %=, **=, //=).

# Bank Account Balance Tracker
# This program allows the user to manage their account balance using assignment operators.

class BankAccount:
    """A simple Bank Account class to manage deposits, withdrawals, and interest calculations."""

    def __init__(self, balance=0):
        """
        Initialize the bank account with a given balance.

        Parameters:
        balance (float): The initial amount in the account. Default is 0.
        """
        self.balance = balance  # Initialize balance

    def deposit(self, amount):
        """
        Deposits an amount into the account.

        Parameters:
        amount (float): The amount to be added.
        """
        self.balance += amount  # Use += operator
        print(f"Deposited: ${amount:.2f} | New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws an amount from the account if sufficient funds are available.

        Parameters:
        amount (float): The amount to be withdrawn.
        """
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount  # Use -= operator
            print(f"Withdrew: ${amount:.2f} | New Balance: ${self.balance:.2f}")

    def apply_interest(self, rate):
        """
        Applies interest to the account balance.

        Parameters:
        rate (float): The interest rate (e.g., 0.05 for 5% interest).
        """
        self.balance *= (1 + rate)  # Use *= operator
        print(f"Interest Applied at {rate * 100:.2f}% | New Balance: ${self.balance:.2f}")

    def apply_fees(self, fee):
        """
        Deducts a fixed fee from the balance.

        Parameters:
        fee (float): The fee amount to be deducted.
        """
        self.balance /= fee  # Use /= operator
        print(f"Fee Applied: {fee} | New Balance: ${self.balance:.2f}")

    def reset_balance(self):
        """Resets the balance to zero using the %= operator."""
        self.balance %= 1  # Use %= operator (sets balance to remainder after division by 1)
        print("Balance reset to zero.")

    def power_balance(self, power):
        """
        Raises the balance to a power.

        Parameters:
        power (int): The exponent to raise the balance to.
        """
        self.balance **= power  # Use **= operator
        print(f"Balance raised to the power of {power} | New Balance: ${self.balance:.2f}")

    def floor_divide_balance(self, divisor):
        """
        Performs floor division on the balance.

        Parameters:
        divisor (int): The number to divide the balance by.
        """
        self.balance //= divisor  # Use //= operator
        print(f"Balance floor divided by {divisor} | New Balance: ${self.balance:.2f}")

    def check_balance(self):
        """Displays the current account balance."""
        print(f"Current Balance: ${self.balance:.2f}")


# Example usage
if __name__ == "__main__":
    account = BankAccount(500)  # Start with $500

    account.deposit(200)  # Deposit $200
    account.withdraw(100)  # Withdraw $100
    account.apply_interest(0.05)  # Apply 5% interest
    account.apply_fees(2)  # Apply fee (dividing balance by 2)
    account.check_balance()  # Check balance
    account.reset_balance()  # Reset balance

#Key Features:
#✅ Uses assignment operators (+=, -=, *=, /=, %=, **=, //=).
#✅ Object-Oriented Programming (OOP) with a BankAccount class.
#✅ Handles deposits, withdrawals, interest, fees, and balance reset.
#✅ Well-documented for HND-level understanding.
