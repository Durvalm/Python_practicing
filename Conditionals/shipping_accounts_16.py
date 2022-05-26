print("Welcome back to your account.\nCurrent prices are as follows.")

# Display prices
print("\nShipping orders 0 to 100: \t\t 5.10$ each")
print("Shipping orders 100 to 500: \t 5.00$ each")
print("Shipping orders 500 to 1000: \t 4.95$ each")
print("Shipping orders over 1000: \t\t 4.80$ each")

# Ask how many items user wants
item_amount = int(input("\nHow many items would you like to ship: "))

# Algorithm for order price
if 0 < item_amount < 100:
    price = item_amount * 5.10
elif 100 < item_amount < 500:
    price = item_amount * 5.00
elif 500 < item_amount < 1000:
    price = item_amount * 4.95
elif item_amount > 1000:
    price = item_amount * 4.80
else:
    print("Wrong input")
    price = None
    quit()

# Price per item
price_per_unit = price/item_amount

# Display final price
print(f"To ship {item_amount} items it will cost you ${price} at a ${price_per_unit} per item")

# Ask if user wants to place the order
choice = input("\nWould you like to place the order (y/n): ")
if choice == 'y':
    print(f"Okay.  Shipping {item_amount} items!")
else:
    print("Okay, order will not be placed at this time!")


