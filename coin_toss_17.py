import random

print("I will flip a coin a set number of times.")
quantity = int(input("How many times would you like me to flip the coin: "))
input("Press enter to see the result of each flip:")
print("\n")

# List of choices
coin = ["TAILS", "HEADS"]

# Count of tails and heads flipped
tail_count = 0
head_count = 0

# Algorithm to randomly flip coins and count them
for i in range(1, quantity+1):
    rand = random.choice(coin)
    print(rand)
    if rand == "TAILS":
        tail_count += 1
    else:
        head_count += 1

    if tail_count == head_count:
        print(f"At {i} flips. the number of heads and tails were equal at {tail_count} each")

# Display results
print(f"\nResults of Flipping a coin {quantity} Times:")
print(f"\nSide              Count            Percentage")
print(f"{coin[0]}             {tail_count}/{quantity}             {tail_count/quantity*100}%")
print(f"{coin[1]}             {head_count}/{quantity}             {head_count/quantity*100}%")
