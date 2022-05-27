import random

# Generate dict for game
dict = {
    "sports": ['soccer', 'basketball', 'baseball'],
    "os": ['macos', 'linux', 'windows'],
}

running = True
while running:
    count = 0
    # Get random key and value from dictionary
    category = random.choice(list(dict.keys()))
    word = random.choice(list(dict[category]))

    # Generated dashed version of word (as a list)
    dashed_word = list('-' * len(word))

    # Print category and dashes for user to try to guess
    print(f"\nGuess a {len(word)} word from the following category: {category}")
    print(f"{''.join(dashed_word)} ")

    # Loop while game tries don't run out
    while count < len(word):
        count += 1
        guess = input(f"\nEnter your guess (Try #{count}): ")

        # If user doesn't guess right, give other chances
        if guess != word:
            print("That is not correct. Let us reveal a letter to help you.")
            # reveal one letter from dashed word
            # Loop is used because we gotta loop until computer finds an index which is not dashed
            while True:
                index = random.randint(0, (len(word) - 1))
                if dashed_word[index] == "-":
                    dashed_word[index] = word[index]
                    print("".join(dashed_word))
                    break
            # If game is over, prompt if user would like to play again
            if count == len(word):
                print("\nYou lost!")
                choice = input("Would you like to play again? (y/n): ").lower()
                if choice == 'y':
                    continue
                else:
                    quit()
        # If user gets word right, prompt if he wants to play again
        else:
            print(f"\nCongratulations, you guessed the word {word}!")
            choice = input("Would you like to play again? (y/n): ").lower()
            if choice == 'y':
                break
            else:
                quit()



