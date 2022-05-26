from collections import Counter

# Initialize poll
poll = input("What is the yes or no issue you will be voting on today: ")
quantity_allowed = int(input("What is the number or voters you will allow on the issue: "))
password = input("What is the password for polling results: ")

# Initialize dict that records voters and their choices
database = {}

# Collect data of voters and votes
for i in range(quantity_allowed):
    voter = input("\nEnter your full name: ").title()
    if voter in database.keys():
        print("You've already voted")
    else:
        print(f"Here is our issue: {poll}")
        choice = input("What do you think... yes or no: ").lower()
        print(f"Thank you {voter}, your answer of {choice} has been recorded.")
        database[voter] = choice

# Display who voted
print(f"\nThe following {len(database.keys())} people voted:")
for i in database.keys():
    print(i)

# counter method
counter = Counter(list(database.values()))

# Algorithm to check which vote won and display who won
print(f"\nOn the following issue: {poll}")
if counter['no'] > counter['yes']:
    print(f"No wins! {counter['no']} votes to {counter['yes']}.")
elif counter['no'] < counter['yes']:
    print(f"Yes wins! {counter['yes']} votes to {counter['no']}.")
else:
    print(f"It's a tie {counter['no']} votes to {counter['yes']}.")

# Ask password to check who voted in what
while True:
    admin_password = input("\nTo see the voting results enter the admin password: ")
    if admin_password == password:
        for key, value in database.items():
            print(f"Voter: {key} \t\t Vote: {value}")
        break
    else:
        print("Not correct, try again!")


