def display_grades(lst, quantity):
    lst.sort()
    print(f"\nGrades Highest to Lowest:")
    for i in lst:
        print(f"\t {i}")

    print("\nGrade Summary:")
    print(f"\t\t Total Number of Grades: {quantity}")
    print(f"\t\t Highest Grade: {max(lst)}")
    print(f"\t\t Lowest Grade: {min(lst)}")
    print(f"\t\t Average: {round(sum(lst) / quantity, 2)}")


grade_quantity = int(input("How many grades would you like to enter: "))

grade_list = []
for i in range(grade_quantity):
    grade_list.append(float(input("Enter grade: ")))

display_grades(grade_list, grade_quantity)
# Ask desired average
desired_average = float(input("\nWhat is your desired average: "))

# Algorithm to reach it
grade_req = round(desired_average * (len(grade_list)+1) - sum(grade_list), 2)
print(f"Good luck, you will need to get {grade_req} in the next test to have an average of {desired_average}")

# Change some grades to see what could have gotten hypothetically
print("\nLet's see what your average could have been if you did better/worse on an assignment.")
grade_list_copy = grade_list[:]
grade_changed = float(input("What grade would you like to change: "))
grade_replacing = float(input(f"What grade would you like to change {grade_changed} to: "))

# Change grades
grade_list_copy.remove(grade_changed)
grade_list_copy.append(grade_replacing)
display_grades(grade_list_copy, grade_quantity)

# Create average variables
grade_average = round(sum(grade_list) / grade_quantity, 2)
grade_copy_average = round(sum(grade_list_copy) / grade_quantity, 2)

# Display difference with changed grade
print(f"\nYour new average would be a {grade_copy_average}"
      f" compared to your real average of {grade_average}!")
print(f"That is a change of {round(grade_copy_average - grade_average,2)} points!")

print(f"\nToo bad your original grades are still the same! \n{grade_list}")
print("You should ask for extra credit")
