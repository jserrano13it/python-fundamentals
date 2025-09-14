def greet_user(name):
    print(f"Hello, {name}! Welcome to EZ ATM")

def calculate_total(initial_balance, deposit_amount):
    return initial_balance + deposit_amount

def withdraw_funds(current_balance, withdrawal_amount):
    return current_balance - withdrawal_amount

def has_sufficient_funds(current_balance, withdrawal_amount):
    return current_balance >= withdrawal_amount

def show_balance(balance):
    print(f"Your current balance is: ${balance}")

# Start the simulation
name_input = input("Enter your name: ")
greet_user(name_input)

pin = input("Enter your 4-digit PIN: ")
if pin != "1234":
    print("Incorrect PIN. Access denied.")
else:
    initial = float(input("Enter your initial balance: "))
    current_balance = initial

    while True:
        print("Select an option:")
        print("1: Show Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(current_balance)
        elif choice == "2":
            deposit = float(input("Enter deposit amount: "))
            current_balance = calculate_total(current_balance, deposit)
            print(f"Deposit successful. New balance: ${current_balance}")
        elif choice == "3":
            withdrawal = float(input("Enter withdrawal amount: "))
            if has_sufficient_funds(current_balance, withdrawal):
                current_balance = withdraw_funds(current_balance, withdrawal)
                print(f"Withdrawal successful. New balance: ${current_balance}")
            else:
                print("Insufficient funds for withdrawal.")
        elif choice == "4":
            print("Thank you for using EZ ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")