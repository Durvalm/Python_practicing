# Get phrase input from user
phrase = input("Enter a word or phrase to count the occurrence of each letter: ").lower()

# list of non letters to be replaced, so we only count letters
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', '?', '!', ',', '"', "'", ':', ':', ';', '(', ')', '%', '$', '&', '#', '\n', '\t']

# Replace non letters in phrase
for non_letter in non_letters:
    phrase = phrase.replace(non_letter, '')

# Calculate phrase length and initialize dict variable
phrase_len = len(phrase)
letter = {}

# put letter and letter count as key and value in dictionary
for i in phrase:
    if i not in letter.keys():
        count = phrase.count(i)
        letter[i] = count

# Display items in dictionary sorted
letter_sorted = sorted(list(letter.keys()))
print("\nHere is the frequency analysis for from key phrase:")
print("Letter / Occurrence / Percentage")
for i in letter_sorted:
    print(f"{i} \t\t\t {letter[i]} \t\t\t {round(letter[i] / phrase_len * 100, 2)}%")

# Display letters ordered from highest occurrence to lowest
print("\nLetters ordered from highest occurrence to lowest")
sort_letters_by_occurrence = sorted(letter.items(), key=lambda x: x[1], reverse=True)
for i in sort_letters_by_occurrence:
    print(i[0], end="")