import math

first_leg = float(input("What is the first leg of the triangle: "))
second_leg = float(input("What is the second leg of the triangle: "))

hypotenuse = round(math.sqrt(first_leg**2 + second_leg**2), 3)
area = round(0.5 * (first_leg * second_leg), 3)

print("\nFor a triangle with legs of {0} and {1} the hypotenuse is {2}.".format(first_leg, second_leg, hypotenuse))
print("For a triangle with legs of {0} and {1} the area is {2}.".format(first_leg, second_leg, area))

