import math
print("A quadratic equation is of the form ax^2 + bx + c = 0")
quantity = int(input("\nHow many equations would you like to solve today: "))

for i in range(quantity):
    print(f"Solving equation #{i+1}")
    print("---------------------------------------------------")
    a = float(input("\nPlease enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient ): "))

    print(f"\nThe solutions to {a}x^2 + {b}x + {c} are:")
    # Quadratic equation formulas
    answer1 = (-b + math.sqrt((b**2) - (4*a*c))) / 2*a
    answer2 = (-b - math.sqrt((b**2) - (4*a*c))) / 2*a

    # Print answers
    print(f"x1 = {answer1}")
    print(f"x2 = {answer2}")
