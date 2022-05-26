def display_values_advanced(start, end):
    """Function that displays values for sliced list of numbers"""
    options = ['Decimal', 'Binary', 'Hexadecimal']
    for option in options:
        print(f"\n{option} values from {start} to {end}")
        for i in range(start, end+1):
            if option == 'Decimal':
                print(i)
            elif option == 'Binary':
                print(bin(i))
            else:
                print(hex(i))


# Get the value in which numbers will be counted up to
max_value = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
print("Generating lists... complete!")

# Get input for sliced result and call function to display it
print("\nUsing slices we will now show a portion of each list.")
slice_start = int(input("What decimal number would you like to start at: "))
slice_end = int(input("What decimal number would you like to stop at: "))

display_values_advanced(slice_start, slice_end)

# Display final result until max_value
input(f"\nPress enter to see all values from 1 to {max_value}")
print("\nDecimal----Binary----hexadecimal")
for i in range(1, max_value + 1):
    print(f"{i}------{bin(i)}------{hex(i)}")
