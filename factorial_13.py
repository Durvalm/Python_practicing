max_number = int(input("What number would you like to compute the factorial of: "))
factorial_lst = list(range(1, max_number+1))

print(f"{max_number}! = ", end="")
print(*factorial_lst, sep="*")

# Algorithm
fact = 1
for i in factorial_lst:
    fact = fact * i

# Display results
print(f"\nHere is the result from my own algorithm:")
print(f"The factorial of {max_number} is {fact}")

