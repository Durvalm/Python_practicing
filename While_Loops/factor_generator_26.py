running = True

# While user wants to run the program, run it
while running:
    # Ask for number
    number = int(input("Enter a number to determine all factors of that number: "))

    # Print the factors of this number
    print(f"\nFactors of {number} are:")
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
            print(i)

    # Display equations without redundancy
    print("\nIn summary:")
    for i in range(int(len(factors)/2)):
        print(f"{factors[i]} * {factors[-i-1]}")

    # Ask if user wants to run the program again
    choice = input("\nRun again? (y/n): ").lower()
    if choice == 'y':
        pass
    else:
        running = False
