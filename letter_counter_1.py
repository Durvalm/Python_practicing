message = input("Enter a message: ").lower()
letter = input("Enter a letter you would like to count: ").lower()
counter = message.count(letter)
print(f"Your message has {counter} letter {letter}'s")


