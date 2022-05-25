def remove_lowest(lst):
    """This function removes the two lowest grades"""
    removed_grades = []
    for value in range(2):
        removed_grades.append(min(lst))
        lst.remove(min(lst))

    return f"Removed grade: {removed_grades[0]}\nRemoved grade: {removed_grades[1]}"


grade_lst = []

grade_1 = float(input("What is your first grade (0-100): "))
grade_2 = float(input("What is your second grade (0-100): "))
grade_3 = float(input("What is your third grade (0-100): "))
grade_4 = float(input("What is your fourth grade (0-100): "))

grade_lst.extend([grade_1, grade_2, grade_3, grade_4])

for i in grade_lst:
    if 100 < i > 0:
        print("You should input a number in between 0 and 100")
        quit()

print("\nYour grades are " + str(grade_lst))
print(f" Your grades sorted are {sorted(grade_lst)}")
print(f"\nThe two lowest grades will now be dropped.")

print(remove_lowest(grade_lst))
print(f"\nYour remaining grades are {grade_lst}")
print(f"Nice work, your highest grade is {max(grade_lst)}")




