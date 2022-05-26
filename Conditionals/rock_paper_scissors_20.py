import random


def check_points(player, computer, game_choice):
    """Function that checks who scored"""
    global player_score, computer_score

    if player == computer:
        print("It is a tie")

    elif player == game_choice[0]:
        if computer == game_choice[1]:
            print("Computer gets the point")
            computer_score += 1
        elif computer == game_choice[2]:
            print("Player gets the point")
            player_score += 1
    elif player == game_choice[1]:
        if computer == game_choice[0]:
            print("Player gets the point")
            player_score += 1
        elif computer == game_choice[2]:
            print("Computer gets the point")
            computer_score += 1
    elif player == game_choice[2]:
        if computer == game_choice[0]:
            print("Computer gets the point")
            computer_score += 1
        elif computer == game_choice[1]:
            print("Player gets the point")
            player_score += 1


# Available choices
game_choices = ['rock', 'paper', 'scissors']

rounds = int(input("How many rounds would you like to play: "))

# Initialize score variables
player_score = 0
computer_score = 0

# Loop until game is finished
for i in range(1, rounds+1):
    print(f"\nRound {i}")
    print(f"Player: {player_score}\t Computer: {computer_score}")

    # Get player and computer choices
    player_choice = game_choices[int(input("Time to pick... rock(0), paper(1), scissors(2): "))]
    computer_choice = game_choices[random.randint(0, 2)]
    print(f"Player: {player_choice}\t Computer: {computer_choice}")

    # Call function that checks results
    check_points(player_choice, computer_choice, game_choices)

# Display results
print("\nFinal game results")
print(f"Rounds played: {rounds}")
print(f"Player Score: {player_score}")
print(f"Computer Score: {computer_score}")
print(f"Winner: ", end="")
if player_score > computer_score:
    print("Player")
else:
    print("Computer")



