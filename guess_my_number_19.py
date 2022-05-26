import random
print("Hello, I'm thinking if a number between 1 and 100...\nYou have 10 tries to guess it.")

# initialize variables
my_num = random.randint(1, 100)
guess_count = 0
tries = 10

# Loop the game until surpasses the amount of tries permitted
while guess_count < tries:

    guess = int(input("\nTake a guess: "))
    guess_count += 1
    # Celebrate if user got the answer right
    if guess == my_num:
        print(f"Congratulations, you guessed the number {my_num} in {guess_count} tries!")
        quit()
    # If answer is not right, tell if it's too low or too high
    else:
        if guess < my_num:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

print(f"\nOver {tries} tries! The number I was thinking was {my_num}")
