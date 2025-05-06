class BankAccount:
    # Class-level attribute to keep track of the next account number to assign
    account_number_generator = 1000
    def __init__(self, account_holder):
        # Initialize instance attributes
        self.account_holder = account_holder  # Name of the account holder
        self.balance = 0.0  # Starting balance (default is 0)
        
        # Increment the shared account number generator and assign a unique account number
        BankAccount.account_number_generator += 1
        self.account_number = BankAccount.account_number_generator

    def deposit(self, amount):
       # Add the specified amount to the account balance.
       # Only positive amounts are allowed.
        if amount > 0:
            self.balance += amount  # Increase balance
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")  # Error message for invalid deposit

    def withdraw(self, amount):
        #Subtract the specified amount from the account balance.
        #The withdrawal amount must be positive and cannot exceed the current balance.
        if 0 < amount <= self.balance:
            self.balance -= amount  # Decrease balance
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")
    
    def display_balance(self):
        #Print the current balance of the account.
        print(f"Current Balance: {self.balance}")
        
      
#Main program starts here
# Display header
print('''
-------------------------------------
|  Bank Account Management System   |
-------------------------------------
''')

# Prompt user for their name and create a new account
name = input("Enter your name: ")  # Capture user input
acc1 = BankAccount(name)  # Instantiate a new BankAccount object
# Display account creation confirmation and details
print(f'''
 Account created successfully!
    -----------------------------------
    |     Here are the details:       |
    -----------------------------------
    Account Number: {acc1.account_number}
    Account Holder: {acc1.account_holder}
    Current Balance: {acc1.balance}
    ''')

    # Menu loop to allow up to 3 transactions or exit early
for i in range(1, 4):
    print('''
    ------------------------------------
    |  1. Deposit                      |
    |  2. Withdraw                     |
    |  3. Display Balance              |
    |  4. Exit                         |
    ------------------------------------
    ''')
        # Display menu options
    try:
       choice = int(input("Enter your choice: ").strip())  # Get menu selection
    except ValueError:
          print("Invalid input. Please enter a number between 1 and 4.")
          continue  # Skip to the next iteration if input is invalid
    if choice == 1:
        # Handle deposit option
        amount = float(input("Enter amount to deposit: "))
        acc1.deposit(amount)
    
    elif choice == 2:
        # Handle withdrawal option
        amount = float(input("Enter amount to withdraw: "))
        acc1.withdraw(amount)
    
    elif choice == 3:
        # Show current balance
        acc1.display_balance()
    
    elif choice == 4:
        # Exit the system
        print("Exiting the system.")
        break
    
    else:
        # Invalid menu option
        print("Invalid choice. Please try again.")
# Final exit message
print('''         You have exited the system
    Thank you for using our Bank Account Management system.\n''')
