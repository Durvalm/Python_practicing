number = float(input("What number would you like to work with: "))


def multiplication(num):
    for i in range(1, 11):
        print(f"{i} * {num} = {round(i*num, 2)}")


def exponent(num):
    for i in range(1, 11):
        print(f"{num} ** {i} = {round(num**i, 2)}")


print(f"\nMultiplication table for {number}")
multiplication(number)
print(f"\nExponent table for {number}")
exponent(number)