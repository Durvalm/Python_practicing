max_value = int(input("What number of the Fibonacci Sequence would you like to compute: "))

# Algorithm FIB
fib = [1, 1]
for i in range(max_value-2):
    fib.append(fib[i] + fib[i+1])

# Algorithm Golden ratio
golden_ratio = []
for i in range(len(fib)-1):
    golden_ratio.append(fib[i+1] / fib[i])

# Display values
print(f"\nThe first {max_value} numbers of the Fibonacci Sequence are: ")
for i in fib:
    print(i)

print(f"\nThe corresponding Golden Ration values are: ")
for i in golden_ratio:
    print(i)