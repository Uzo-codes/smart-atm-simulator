#Global state
USER_PIN = '1234'
balance = 30000

#Function to handle user login
def login():
    print("Welcome to the smart atm")

    #Allow user 3 attempts to enter the correct PIN
    for attempt in range(3):
        pin = input("Please enter your 4 digit pin: ")
        
        if pin == USER_PIN:
            print("Login Successful! \n")
            return True
        
        else:
            print("Incorrect PIN. Try again.")

        #If all attempts fail
        print("Too many failed attempts. Card blocked.")
        return False
    
#Display the menu options
def show_menu():
    print("\n ATM MENU ")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit ")
    print("4. Exit")

#Check the current balance
def check_balance():
    print(f"Your current balance is: {balance:,}")

#Withdraw from account
def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficient Funds.")
    elif amount <= 0:
        print("Invalid withdrawal amount.")
    else:
        balance -= amount
        print(f"You withdrew {amount:,}. New balance: {balance:,}")

#Deposit into account
def deposit(amount):
    global balance

    if amount <= 0:
        print("Invalid deposit amount.")
    else:
        balance += amount
        print(f"You deposited {amount:,}. New balance: {balance:,}")

#Main ATM loop
def run_atm():
    if not login():
        return
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            check_balance()

        elif choice == '2':
            try:
                amount = int(input("Enter amount to withdraw: "))
                withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            try:
                amount = int(input("Enter amount to deposit: "))
                deposit(amount)
            except ValueError:
                print("Please enter a valid number")

        elif choice == '4':
            print("Thank you for using smart ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1-4.")

#Run the ATM app
run_atm()
