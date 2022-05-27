running = True

while running:
    # Get user input
    numbers = input("Enter in a string of numbers separated by a comma (,): ").strip().split(",")

    # Transform string into single list of numbers
    new_list = []
    for i in numbers:
        j = i.replace(" ", "")
        new_list.append(j)

    # Create a list to store every even or odd numbers
    even = []
    odd = []

    # Print result of evens and odds and append odd to its list and even to its list
    print("\n---- Result Summary ----")
    for i in new_list:
        if int(i) % 2 == 0:
            print(f"\t {i} is even!")
            even.append(i)
        else:
            print(f"\t {i} is odd!")
            odd.append(i)

    # Print even and odds separately
    print(f"\nThe following {len(even)} numbers are even: ")
    for i in even:
        print(f"\t {i}")

    print(f"\nThe following {len(odd)} numbers are odd: ")
    for i in odd:
        print(f"\t {i}")

    # Ask if user wants to run again
    choice = input("Would you like to run the program again? (y/n): ")
    if choice == 'y':
        pass
    else:
        running = False


