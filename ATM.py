import time

# Initialize transaction history
transaction_history = []

print("Welcome to the ATM interface")
print("Please insert your card")
time.sleep(5)
User_ID = int(input("Enter the ID of user"))
PIN = int(input("Enter the PIN: "))
print("==============================================")
balance = 5000

if User_ID == 12345 and PIN == 67890:
    print("Login Successful!!!\n")
    while True:
        print("""ATM Operations:
              1. Check Balance
              2. Withdraw
              3. Deposit
              4. Transfer
              5. Transaction History
              6. Quit
              """)
        try:
            option = int(input("Please enter your choice: "))
            print("==============================================")
        except Exception as e:
            print(f"Please enter a valid option: {e}")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")
            print("==============================================")

        elif option == 2:
            withdraw_amount = int(input("Please enter amount to withdraw: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                transaction_history.append(f"Withdrew {withdraw_amount}")
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {balance}")
            else:
                print("Insufficient balance")
            print("==============================================")

        elif option == 3:
            deposit_amount = int(input("Please enter amount to deposit: "))
            balance += deposit_amount
            transaction_history.append(f"Deposited {deposit_amount}")
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")
            print("==============================================")

        elif option == 4:
            transfer_amount = int(input("Please enter amount to transfer: "))
            if transfer_amount <= balance:
                recipient_acc = input(
                    "Please enter the recipient account number: ")
                balance -= transfer_amount
                transaction_history.append(
                    f"Transferred {transfer_amount} to acc {recipient_acc}")
                print(
                    f"{transfer_amount} is transferred to acc {recipient_acc}")
                print(f"Your updated balance is {balance}")
            else:
                print("Insufficient balance")
            print("==============================================")

        elif option == 5:
            print("Transaction History:")
            if transaction_history:
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")
            print("==============================================")

        elif option == 6:
            print("Thank you for using the ATM. Have a Good day!")
            break

        else:
            print("Invalid option, please try again.")
else:
    print("Wrong pin. Please try again.")
