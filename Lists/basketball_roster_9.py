import random
print("Welcome to the Basketball Roster Program")


# Function that displays roster
def display_roster(lst):
      print(f"\n\t\t Your starting {len(roster)} for the upcoming basketball season")
      print(f"\t\t\t Point Guard:\t\t {roster[0]}"
            f"\n\t\t\t Shooting Guard:\t {roster[1]}"
            f"\n\t\t\t Small Foward:\t\t {roster[2]}"
            f"\n\t\t\t Power Forward:\t\t {roster[3]}"
            f"\n\t\t\t Center:\t\t\t {roster[4]}\n ")


# Variable for Roster
roster = []

# Get input for all 5 players in roster
player_1 = input("\nWho is your point guard: ").capitalize()
player_2 = input("Who is your shooting guard: ").capitalize()
player_3 = input("Who is your small forward: ").capitalize()
player_4 = input("Who is your power forward: ").capitalize()
player_5 = input("Who is your center: ").capitalize()

# Put all players in roster and call function to display roster
roster.extend([player_1, player_2, player_3, player_4, player_5])
display_roster(roster)

# Injure random player using random index and remove from roster
injured_player_index = random.randint(0, 4)
injured_player_name = roster[injured_player_index]
print(f"\nOh no, {injured_player_name} is injured.")
roster.remove(injured_player_name)
print(f"Your roster has only {len(roster)} players ")

# Ask who will replace the injured player and insert it in the same position using the index gotten to remove it
new_player = input(f"Who will take {injured_player_name}'s spot: ").capitalize()
roster.insert(injured_player_index, new_player)

# Display roster and say good luck
display_roster(roster)
print(f"Good luck, {new_player} will do great!")
print(f"Your roster now has {len(roster)} players.")




