import random

# list of synonyms (thesaurus)
synonyms = {
    'hot': ['balmy', 'summery', 'tropical', 'boiling'],
    'cold': ['chilly', 'cool', 'freezing', 'frigid'],
    'happy': ['content', 'cheery', 'merry', 'jovial'],
    'sad': ['unhappy', 'downcast', 'miserable', 'glum'],
}

# Display words available to see synonyms of
print("Choose a word from the thesaurus and I will give you a synonym")
print("\nhere are the words in the thesaurus:")
for key in synonyms.keys():
    print(f"\t\t -{key}")

# get input from user of what word he'd like to see the synonym of
word = input("\nWhat word would you like a synonym for: ").lower()

# get random word inside list of synonyms in dict
value = random.choice(synonyms[word])

# Display synonym requested
if word not in synonyms.keys():
    print("Word not found, try again.")
else:
    print(f"A synonym for {word} is {value}!")

# Show whole thesaurus if user wants
choice = input("\nWould you like to see the whole thesaurus (y/n): ")
if choice == 'y':
    for key, value in synonyms.items():
        print(f"\n{key} synonyms are:")
        for i in value:
            print(f"\t\t - {i}")
else:
    quit()
