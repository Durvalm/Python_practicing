# Get user input
principal = float(input("Enter the loan amount: "))
interest = float(input("Enter the interest rate: "))
monthly_pay = float(input("Enter the desired monthly payment amount: "))
money_paid = 0

# Dictionary to store data
loan_info = {
    'principal': principal,
    'interest': interest,
    'monthly_pay': monthly_pay,
    'money_paid': money_paid,
}


def display_info(loan, count_):
    """This function displays info about loan"""
    print(f"\nLoan information after {count_} months")
    print(f"Principal: {loan['principal']}")
    print(f"Rate: {loan['interest']}")
    print(f"Monthly Payment: {loan['monthly_pay']}")
    print(f"Money Paid: {loan['money_paid']}")


def calculate(loan):
    """This function does all the work of updating values in loan_info"""

    # algorithm to decrement principal
    loan['principal'] += loan['principal'] * ((loan['interest'] / 100) / 12)
    # Increment principal with monthly payment
    loan['principal'] -= loan['monthly_pay']

    if loan['principal'] < 0:
        loan['money_paid'] += loan['monthly_pay'] + loan['principal']
        loan['principal'] = 0

    else:
        loan['money_paid'] += loan['monthly_pay']


# initialize program
count = 0
display_info(loan_info, count)
input("Press 'Enter' to begin paying off your loan.")

while loan_info['principal'] != 0:
    # Call functions to increment values in dictionary
    count += 1
    calculate(loan_info)
    display_info(loan_info, count)

    # Quit if loan is not payable with current monthly payment
    if loan_info['principal'] > principal:
        print("\nYou will NEVER pay off your loan!!!\nYou cannot get ahead of the interest!")
        quit()

# Display info after loan is paid
print(f"\nCongratulations, you pais off your loan in {count} months!"
      f"\nYour initial loan was {principal} at a rate of {interest}%."
      f"\nYour monthly payment was ${monthly_pay}."
      f"\nYou spent ${round(loan_info['money_paid'], 2)} in total."
      f"\nYou spent ${round(loan_info['money_paid'] - principal, 2)} in interest!")

