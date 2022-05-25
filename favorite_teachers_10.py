def fav_teachers(lst):
    """This function displays fav teachers"""
    print(f"\nYour favorite teachers ranked are: {lst}")
    print(f"Your favorite teachers alphabetically are: {sorted(lst)}")
    print(f"Your favorite teachers in reverse alphabetical order are: {sorted(lst, reverse=True)}")

    # Show teachers by ranking
    print(f"\nYour top 2 teachers are: {lst[0]} and {lst[1]}")
    print(f"Your next 2 favorite teachers are: {lst[2]} and {lst[3]}")
    print(f"Your last favorite teacher is {lst[-1]}")
    print(f"You have a total of {len(lst)} favorite teachers")


# ask user input for favorite teachers in order
teacher1 = input("Whats your favorite teacher: ").capitalize()
teacher2 = input("Whats your second favorite teacher: ").capitalize()
teacher3 = input("Whats your third favorite teacher: ").capitalize()
teacher4 = input("Whats your fourth favorite teacher: ").capitalize()

teacher_rank = []

# Add input to the list and call function to display teacher list
teacher_rank.extend([teacher1, teacher2, teacher3, teacher4])
fav_teachers(teacher_rank)

# Favorite teacher is no longer favorite teacher
print(f"\n{teacher_rank[0]} is no longer your favorite teacher.")
new_fav_teacher = input("Who is your new FAVORITE teacher: ").capitalize()

# Put new favorite teacher as the first one in rank list
teacher_rank.insert(0, new_fav_teacher)

# Call function to display teacher list again
fav_teachers(teacher_rank)

# User decided he doesn't like a teacher, get input and remove it from least
while True:
    removed_teacher = input("\nYou have decided you no longer like a teacher, "
                            "which teacher would you like to remove from the list: ").capitalize()
    if removed_teacher in teacher_rank:
        teacher_rank.remove(removed_teacher)
        break
    else:
        print("Enter a valid teacher from the list")

# Call function to display teacher list again
fav_teachers(teacher_rank)


