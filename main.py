from bank_account import BankAccount

if __name__ == "__main__":
    my_account = BankAccount()
    
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Change Password")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            my_account.deposit()
        elif choice == "2":
            my_account.withdraw()
        elif choice == "3":
            my_account.check_balance()
        elif choice == "4":
            my_account.change_password()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
