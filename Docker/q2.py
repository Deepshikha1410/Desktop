"""create a Class Bank Account. The class should have the following attribute : Account Number,
account Holder name, Account type, and balance. Implement methods to get and set each attribute 
additionally, create a method that prints out the account details in a redable format..... """


class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder_name(self):
        return self.account_holder_name

    def set_account_holder_name(self, account_holder_name):
        self.account_holder_name = account_holder_name

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def print_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance:.2f}")

# Example usage
account = BankAccount(123456789, "sagar", "Savings", 4000)
account = BankAccount(123456789, "jeet", "Savings", 2000)
account = BankAccount(123456789, "abhi", "Savings", 3000)
account = BankAccount(123456789, "suhas", "Savings",5000)
account.print_account_details()