import random


def generate_ticket(white_ball, red_ball, lst):
    """Algorithm that generates random 6 number tickets and only returns if ticket has not been bought before"""
    my_bet = []

    while len(my_bet) < 5:
        num = random.randint(1, white_ball)
        if num not in my_bet:
            my_bet.append(num)
    my_bet.sort()
    my_bet.append(random.randint(1, red_ball))

    # Return if my_bet not in list
    if my_bet not in lst:
        return my_bet
    else:
        return "Disregard"


# Get input from user
white_ball_max = int(input("How many white-balls to draw from for the 5 winning numbers (normally 69): "))
red_ball_max = int(input("How many red-balls to draw from for the Power-Ball (normally 26): "))

# Algorithm to calculate odds of winning
odds = 1
for i in range(5):
    odds *= white_ball_max - i
odds *= red_ball_max/120

# Print chances of winning
print(f"You have a 1 in {odds} chance of winning this lottery")

# Determining interval for purchasing tickets
interval = int(input("Purchase tickets in what interval: "))

# Determining white winning numbers
winning_numbers = []
while len(winning_numbers) < 5:
    number = random.randint(1, white_ball_max)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()
# append red ball winning number to winning number list
winning_numbers.append(random.randint(1, red_ball_max))

# Display information to user
print("\n------- Welcome to the Power-Ball -------")
print("Tonight's winning numbers are: ", end='')
print(*winning_numbers)
input("Press 'Enter' to begin purchasing tickets!!! ")

# Simulate powerball
interval_count = 0
continuous_count = 0
list_of_tries = []

while True:
    # Call function that generates list
    my_list = generate_ticket(white_ball_max, red_ball_max, list_of_tries)

    # if returned value in function is a list, perform following actions
    if type(my_list) == list:
        list_of_tries.append(my_list)
        print(my_list)
        interval_count += 1
        continuous_count += 1

        # If user's ticket is the same as the winning ticket, tell user that he won
        if my_list == winning_numbers:
            print(f"Congratulations, after {continuous_count} times you won the prize!")
            quit()

    # If tickets bought are not winning tickets, ask if user would like to run program again
    if interval_count >= interval:
        choice = input(f"Would you like to spin {interval} times again? (y/n): ").lower()
        if choice == 'y':
            interval_count = 0
            continue
        else:
            break

