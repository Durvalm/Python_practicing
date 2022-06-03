import random
game_board = {'1': '-', '2': '-', '3': '-', '4': '-', '5': '-', '6': '-', '7': '-', '8': '-', '9': '-'}


def display_game_board(game_boar):
    return "\tTic-Tac-Toe" \
           "\n-----------------" \
           "\n|| 1 || 2 || 3 ||" \
           "\n-----------------" \
           "\n|| 5 || 6 || 6 ||" \
           "\n-----------------" \
           "\n|| 7 || 8 || 9 ||" \
           "\n-----------------\n\n" \
            "\tTic-Tac-Toe" \
           "\n-----------------" \
           f"\n|| {game_boar['1']} || {game_boar['2']} || {game_boar['3']} ||" \
           "\n-----------------" \
           f"\n|| {game_boar['4']} || {game_boar['5']} || {game_boar['6']} ||" \
           "\n-----------------" \
           f"\n|| {game_boar['7']} || {game_boar['8']} || {game_boar['9']} ||" \
           "\n-----------------\n" \



def play(game_boar, x_or_y_):
    """This function gets input from user (X or Y) and places piece into dictionary"""
    while True:
        choice = input(f"{x_or_y_}: What number would you like to place: ")
        if game_boar[choice] == '-':
            game_boar[choice] = x_or_y_
            break
        else:
            print("Position has been already chosen, try again.")


def check_results(game_boar):
    """This function checks if user won"""
    lst = list(game_boar.values())

    # Check for X
    if lst[0] == 'X' and lst[1] == 'X' and lst[2] == 'X':
        return 'X'
    if lst[3] == 'X' and lst[4] == 'X' and lst[5] == 'X':
        return 'X'
    if lst[6] == 'X' and lst[7] == 'X' and lst[8] == 'X':
        return 'X'
    if lst[0] == 'X' and lst[4] == 'X' and lst[8] == 'X':
        return 'X'
    if lst[2] == 'X' and lst[4] == 'X' and lst[6] == 'X':
        return 'X'

    # Check for Y
    if lst[0] == 'Y' and lst[1] == 'Y' and lst[2] == 'Y':
        return 'Y'
    if lst[3] == 'Y' and lst[4] == 'Y' and lst[5] == 'Y':
        return 'Y'
    if lst[6] == 'Y' and lst[7] == 'Y' and lst[8] == 'Y':
        return 'Y'
    if lst[0] == 'Y' and lst[4] == 'Y' and lst[8] == 'Y':
        return 'Y'
    if lst[2] == 'Y' and lst[4] == 'Y' and lst[6] == 'Y':
        return 'Y'


# Initialize game
round = 1
print(f"\nRound {round}:")
table = display_game_board(game_board)
print(table)

# Loop through rounds
while True:
    # if round is even: player X will play, if odd: player Y will.
    if round % 2 == 0:
        x_or_y = 'Y'
    else:
        x_or_y = 'X'

    # Increment round variable
    round += 1

    # Call play function to allow user to play
    play(game_board, x_or_y)

    # Print the game on the screen
    print(f"\nRound {round}:")
    table = display_game_board(game_board)
    print(table)

    # Check results and return if user won
    winner = check_results(game_board)
    if winner is not None:
        print(f"{winner} won!")
        break
