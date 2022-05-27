import time
running = True

while running:
    # Ask if user wants 1 or 2
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = input("Enter your choice 1 or 2: ")

    # If single number is prime
    if choice == '1':
        numb = int(input("\nEnter a number to determine if it is prime or not: "))

        # Algorithm
        is_prime = True

        for i in range(2, numb):
            if numb % i == 0:
                is_prime = False

        # Display if it's prime or not
        if is_prime:
            print(f"{numb} is prime!")
        else:
            print(f"{numb} is not prime!")

    # All primes in a range
    elif choice == '2':
        # Get input for lower and upper bound
        lower_bound = int(input("\nEnter the lower bound of your range: "))
        upper_bound = int(input("Enter the upper bound of your range: "))

        # Algorithm with nested for loops to check all numbers
        start_time = time.time()
        primes = []
        for number in range(lower_bound, upper_bound+1):
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                if number not in primes and is_prime:
                    primes.append(number)

        # Calculate calculation time
        end_time = time.time()
        calc_time = round(end_time - start_time, 7)

        # Display primes
        print(f"\nCalculations took a total of {calc_time} seconds")
        print(f"The following numbers between {lower_bound} and {upper_bound} are prime:")
        input("Press enter to continue:")
        for i in primes:
            print(i)

    # In case user enters a command other than 1 and 2
    else:
        print("Number is not valid")
        continue

    # Ask if user wants to run the program again
    choice = input("\nWould you like to run the program again (y/n): ").lower()
    if choice == 'y':
        continue
    else:
        running = False


