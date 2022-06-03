def get_info():
    """Get user input and creates bank account"""

    name = input("What is your name: ").title()
    savings = int(input("How much would you like to set up your savings account with: "))
    checking = int(input("How much would you like to set up your checking account with: "))

    bank_account = {
        'name': name,
        'savings': savings,
        'checking': checking,
    }

    return bank_account


def display_info(bank_account):
    print("\nCurrent Account Information")
    print(f"Name: {bank_account['name']}"
          f"\nSavings: ${bank_account['savings']}"
          f"\nChecking: ${bank_account['checking']}")


def make_deposit(bank_account, account, money):
    bank_account[account] += money
    print(f"Deposited ${money} into {bank_account['name']}'s {account} account.")


def make_withdraw(bank_account, account, money):
    bank_account[account] -= money
    print(f"Withdrew ${money} from {bank_account['name']}'s {account} account.")


# Main code
bank = get_info()

while True:
    # Get input about transaction
    account_type = input("\nWhat account would you like to access? (Savings or Checking): ").lower()
    transaction_type = input("What type of transaction would you like to make (Deposit or Withdraw): ").lower()
    transaction_amount = float(input("How much money: "))

    if account_type == "savings" or account_type == "checking":
        if transaction_type == 'deposit':
            make_deposit(bank, account_type, transaction_amount)
        elif transaction_type == 'withdraw':
            make_withdraw(bank, account_type, transaction_amount)
        else:
            print("Failed to make transaction! only (deposit/withdraw)")
    else:
        print("Error, only (savings/checking)")

    # Display info function
    display_info(bank)

    # Ask if user wants
    choice = input("Would you like to make another transaction? (y/n): ")
    if choice == 'y':
        continue
    else:
        print("\nThank you.  Have a great day!")
        break
