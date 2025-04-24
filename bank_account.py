class BankAccount:
    def __init__(self):
        print("Welcome to Cairo Bank!")
        self.name = input("Enter Your Name: ")
        self.password = input("Enter Your Password: ")
        self.national_id = int(input("Enter Your National ID: "))
        self.credit = 0

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.credit += amount
        print(f"Deposit successful. Current balance: {self.credit}")

    def withdraw(self):
        input_password = input("Enter your password: ")
        if input_password == self.password:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.credit:
                self.credit -= amount
                print("Withdrawal successful.")
            else:
                print(f"Insufficient funds. Current balance: {self.credit}")
        else:
            print("Incorrect password.")

    def check_balance(self):
        print(f"Current balance: {self.credit}")

    def change_password(self):
        old_password = input("Enter old password: ")
        if old_password == self.password:
            self.password = input("Enter new password: ")
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")
