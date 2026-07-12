transactions_history=[]
current_user = None
logged_in = False
def menu():
    print("========= BANK =========")
    print("1. Create Account")
    print("2. Login")
    print("3. Check Balance")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Transfer Money")
    print("7. Transaction History")
    print("8. Logout")
    print("9. Exit")
def create_account():
    name = input("Enter your name: ")
    pin = input("Create a 4-digit PIN: ")
    
    
    global balance
    balance = float(input("Enter your starting balance: "))
    with open("AccountDetails.txt", "a") as file:
        file.write(f"{name}:{pin}:{balance}\n")
    print("Welcome,", name)
    print("Your account has been created!")
def login():
    name = input("Enter your name: ")
    pin = input("Enter your 4-digit PIN: ")

    found = False

    with open("AccountDetails.txt", "r") as file:
        for line in file:
            saved_name, saved_pin, saved_balance = line.strip().split(":")
            print("Entered:", name, pin)
            print("Saved:", saved_name, saved_pin)

            if name == saved_name and pin == saved_pin:
                print("Login successful!")
                found = True
                global balance
                global current_user
                global logged_in
                current_user = name
                logged_in = True
                balance = float(saved_balance)
                break

    if not found:
        print("Incorrect username or PIN.")
def check_balance():
    if not logged_in:
        print("Please log in to check your balance.")
        return
    global balance
    print(f"Your current balance is ${balance}")        
def deposit():
    if not logged_in:
        print("Please login first.")
        return

    global balance

    amount = float(input("Amount: "))
    balance += amount

    transactions_history.append(f"Deposited ${amount}")

    with open("AccountDetails.txt", "r") as file:
        lines = file.readlines()

    with open("AccountDetails.txt", "w") as file:
        for line in lines:
            saved_name, saved_pin, saved_balance = line.strip().split(":")

            if saved_name == current_user:
                file.write(f"{saved_name}:{saved_pin}:{balance}\n")
            else:
                file.write(line)

    print("Deposit successful!")
def withdraw():
    if not logged_in:
        print("Please log in to withdraw money.")
        return
    amount = float(input("Enter the amount to withdraw: "))
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        transactions_history.append(f"Withdrawn ${amount}")

    with open("AccountDetails.txt", "r") as file:
        lines = file.readlines()

    with open("AccountDetails.txt", "w") as file:
        for line in lines:
            saved_name, saved_pin, saved_balance = line.strip().split(":")

            if saved_name == current_user:
                file.write(f"{saved_name}:{saved_pin}:{balance}\n")
            else:
                file.write(line)

    print("Withdrawal successful!")

def transfer():
    if not logged_in:
        print("Please log in to transfer money.")
        return

    global balance

    recipient = input("Enter the recipient's name: ")
    amount = float(input("Enter the amount to transfer: "))

    if amount > balance:
        print("Insufficient funds!")
        return

    balance -= amount

    transactions_history.append(
        f"Transferred ${amount} to {recipient}"
    )

    with open("AccountDetails.txt", "r") as file:
        lines = file.readlines()

    with open("AccountDetails.txt", "w") as file:
        for line in lines:
            saved_name, saved_pin, saved_balance = line.strip().split(":")

            if saved_name == current_user:
                file.write(f"{saved_name}:{saved_pin}:{balance}\n")
            else:
                file.write(line)

    print("Transfer successful!")
    print(f"${amount} has been transferred to {recipient}.")
    print(f"Your new balance is ${balance}")
def transaction_history():
    if not logged_in:
        print("Please log in first.")
        return

    print("\n===== Transaction History =====")

    if len(transactions_history) == 0:
        print("No transactions yet.")
        return

    for transaction in transactions_history:
        print(transaction)
while True:
    menu()
    choice = input("Choose an option: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        deposit()
    elif choice == "5":
        withdraw()
    elif choice == "6":
        transfer()
    elif choice == "7":
        transaction_history()
    elif choice == "8":
        logged_in = False
        current_user = None
        print("You have been logged out.")
    elif choice == "9":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
