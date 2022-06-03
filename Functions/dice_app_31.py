import random


def side_input():
    side = int(input("How many sides would you like on your dice: "))
    return side


def dice_input():
    dice = int(input("How many dice would you like to roll: "))
    return dice


def roll(side, dice):
    lst_of_dices = []
    for j in range(dice):
        lst_of_dices.append(random.randint(1, side))
    return lst_of_dices


# Call functions to receive input
sides = side_input()
dices = dice_input()

# Print results
print("\n-----Results are as followed-----")
lst_of_dice = roll(sides, dices)
for i in lst_of_dice:
    print(i)
print(f"The total value of your roll is {sum(lst_of_dice)}")