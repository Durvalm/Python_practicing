import datetime


def add_food(lst):
    """Function to add food to the grocery list until the list has 5 items"""
    while len(lst) < 5:
        food = input("Type of food to add to grocery list: ").capitalize()
        lst.append(food)


def grocery_simulation(lst):
    """Function that simulates user buying items from list"""
    # allow user to buy until list has 2 items
    while len(lst) > 2:
        print(f"\nCurrent grocery list: {len(lst)} items")
        print(sorted(lst))
        food_purchased = input("What food in the list would you like to buy: ").capitalize()
        # If user tries the buy product not in the list, throw an error
        if food_purchased not in lst:
            print("This item is not in your list")
        # If user buys item from list, remove it from the list
        else:
            print(f"Removing {food_purchased} from list...")
            lst.remove(food_purchased)

    # shows that an item is out of stock when list reaches 2 items
    while True:
        print(f"\nCurrent grocery list: {len(lst)} items\n{lst}")
        # Store is out of last item in the list
        print(f"\nSorry, the store is out of {lst[-1]}.")
        # Ask what food user would like to replace the one out of stock with, and put in in list
        food = input("What food would you like instead (not from the list): ").capitalize()
        if food not in lst:
            lst[-1] = food
            break
        # if user chooses an item already in the list, continue looping
        else:
            print("Choose an item not from the list")


date = datetime.datetime.now()
# Initialize food list with 2 items
food_list = ['Meat', 'Cheese']

print("Welcome to the Grocery List App.")
print(f"Current Date and Time: {date.strftime('%x')} \t{date.strftime('%X')}")

print(f"You currently have {food_list[0]} and {food_list[1]} in your list\n")

add_food(food_list)

print("\nHere is your grocery list:")
print(food_list)
print(f"Here is your grocery list sorted:\n{sorted(food_list)}")

print("\nSimulating grocery shopping:")
grocery_simulation(food_list)
print(f"\nHere is what remains in your list:\n{food_list}")
