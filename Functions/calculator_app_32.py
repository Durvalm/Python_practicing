def get_input():
    first_num = float(input("\nEnter a number: "))
    second_num = float(input("Enter a number: "))
    operation_type = input("Enter an operation (addition = [+], subtraction = [-], "
                               "multiplication = [*], division = [/], exponentiation = [**]): ")
    return first_num, second_num, operation_type


def operation(first_numb, second_numb, operation_typ):
    result = None
    if operation_typ == '+':
        result = first_numb + second_numb
    elif operation_typ == '-':
        result = first_numb - second_numb
    elif operation_typ == '*':
        result = first_numb * second_numb
    elif operation_typ == '/':
        result = first_numb / second_numb
    elif operation_typ == '**':
        result = first_numb ** second_numb
    else:
        return "Wrong operation type"

    return f"{first_numb} {operation_typ} {second_numb} = {result}"


print("Enter two numbers and an operation and the desired operation will be performed.")

lst_of_equations = []
while True:
    a, b, c = get_input()
    resul = operation(a, b, c)
    lst_of_equations.append(resul)

    choice = input("Would you like to run the program again? (y/n): ")
    if choice == 'y':
        continue
    else:
        print("\nHere are all the equations you've performed...")
        [print(i) for i in lst_of_equations]
        break

