# List of available parties
parties = ('Republican', 'Democratic', 'Libertarian', 'Independent', 'Green')

# Ask for user input
name = input("What's your name: ").capitalize()
age = int(input("What's your age: "))

# Check if user is old enough to vote
if age < 18:
    print("You are not old enough to vote")
    quit()
else:
    print(f"Congratulations {name}, you are old enough to vote!")
    pass

# Display list of parties
print("\nHere is a list of political parties to join.")
for party in parties:
    print(f"\t\t - {party}")

# Ask for which party user wants to join
while True:
    party_choice = input("\nWhat party would you like to join: ").capitalize()
    if party_choice not in parties:
        print("You must join a valid party, check for spelling.")
    else:
        print(f"\nCongratulations {name}, you have joined the {party_choice} party!")
        break

# Print message about party chosen
for i in parties:
    if party_choice == i:
        if i == parties[0] or parties[1]:
            print("That is a major party")
        else:
            print("That is not a major party")

