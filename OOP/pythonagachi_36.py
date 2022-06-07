import random
import time


class Creature:
    """This class simulates a creature and its life in the game"""
    def __init__(self, name):
        self.name = name.title()
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food_inventory = 2
        self.is_sleeping = False
        self.is_alive = True

    def forge_food(self):
        # Randomly find food from 0 to 4 peaces
        food_found = random.randint(0, 4)
        self.food_inventory += food_found

        # Increment dirtiness
        self.dirtiness += 2

        print(f"{self.name} found {food_found} pieces of food")

    def eat(self):
        # Decrement food inventory and hunger
        if self.food_inventory > 0:
            self.food_inventory -= 1
            self.hunger -= random.randint(1, 4)
            print(f"Yum, {self.name} ate a great meal!")
        else:
            print(f"{self.name} doesn't have any food, better forage for some.")

        # If hunger is less than 0, set it to 0
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        print(f"\n{self.name} wants to play a game")
        print(f"{self.name} is thinking of a number 0, 1, or 2.")

        # Creature's number
        number = random.randint(0, 2)
        guess = int(input("What's your guess: "))

        if guess != number:
            print(f"Wrong, {self.name} was thinking of {number}")
            self.boredom -= 1
        else:
            print(f"Nice, you guessed the number {number}")
            self.boredom -= 3

        # if boredom is less than zero, set it to zero
        if self.boredom < 0:
            self.boredom = 0

    def bath(self):
        self.dirtiness = 0
        print(f"{self.name} has taken a bath. All clean!")

    def sleep(self):
        # Put the creature to sleep
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        print("Zzzzz.....Zzzzzz....Zzzzzz.....")

        # if tiredness or boredom is less than zero, set it to zero
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0

    def awake(self):
        # creature has 1/3 chance to wake up
        value = random.randint(0, 2)
        if value == 0:
            # if creature wake up set tiredness to 0
            print(f"{self.name} just woke up!")
            self.is_sleeping = False
            self.tiredness = 0
        else:
            print(f"{self.name} won't wake up!")
            self.sleep()

    def show_values(self):
        print(f"\nCreature Name: {self.name}")
        print(f"Hunger (0-10): {self.hunger}")
        print(f"Boredom (0-10): {self.boredom}")
        print(f"Tiredness (0-10): {self.tiredness}")
        print(f"Dirtiness (0:10): {self.dirtiness}")

        print(f"\nFood Inventory: {self.food_inventory} pieces")
        if self.is_sleeping:
            print(f"Current Status: Sleeping")
        else:
            print(f"Current Status: Awake")

    def increment_values(self, diff):
        """user must set an arbitrary difficulty, This will control how much damage pet takes"""
        # Increase the hunger and dirtiness regardless if the creature is awake or sleeping
        self.hunger += random.randint(0, diff)
        self.dirtiness += random.randint(0, diff)

        # If the creature is awake, he should be growing tired and growing bored
        if not self.is_sleeping:
            self.boredom += random.randint(0, diff)
            self.tiredness += random.randint(0, diff)

    def kill(self):
        if self.hunger >= 10:
            print(f"\n{self.name} starved to death...")
            self.is_alive = False
        elif self.dirtiness >= 10:
            print(f"\n{self.name} has suffered an infection and died...")
            self.is_alive = False
        if self.tiredness >= 10:
            self.tiredness = 10
            print(f"\n{self.name} is sleepy. Falling asleep...")
            self.is_sleeping = True
        if self.boredom >= 10:
            self.boredom = 10
            print(f"\n{self.name} is bored Falling asleep...")
            self.is_sleeping = True

    @staticmethod
    def game_options():
        if creature.is_sleeping:
            choice = input("\nEnter (6) to try and wake up.")
            choice = 6
        # Creature is awake, give full functionality
        else:
            print(f"\nEnter (1) to eat.")
            print(f"Enter (2) to play.")
            print(f"Enter (3) to sleep.")
            print(f"Enter (4) to take a bath.")
            print(f"Enter (5) to forage for food.")
            choice = input("What is your choice: ")

        return choice

    @staticmethod
    def call_action(choice):
        if choice == '1':
            creature.eat()
        elif choice == '2':
            creature.play()
        elif choice == '3':
            creature.sleep()
        elif choice == '4':
            creature.bath()
        elif choice == '5':
            creature.forge_food()
        elif choice == '6':
            creature.awake()
        else:
            print("Invalid input!")


# Main game
print("Welcome to the Pythonagachi Simulator App")
difficult = int(input("Choose a difficulty level (1-5): "))
name = input("What name would you like to give your pet: ").title()

creature = Creature(name)
count = 0
while creature.is_alive:
    count += 1
    print(f"\n---------------------------------------------------\nRound #{count}")
    creature.show_values()
    option = creature.game_options()
    creature.call_action(option)

    # Summary
    print(f"\nRound #{count} Summary:")
    creature.show_values()
    print("Advancing to next round...")
    time.sleep(4)
    creature.increment_values(difficult)
    creature.kill()

print("\nR.I.P")
print(f"{creature.name} survived a total of {count} rounds")


