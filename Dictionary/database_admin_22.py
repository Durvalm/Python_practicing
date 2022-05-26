# Initialize database with an admin and populate other fields
database = {
    'admin': 'admin',
    'fur3nfou3r': 'fbubf',
    '3fubof': 'uy3gf',
    'marcos': 'f3ouf',
    '3fo3ufh': 'inrio',
}

# Ask user for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# If username and password correspond to admin, show database
if username == 'admin' and password == 'admin':
    print("\nWelcome admin, here is the current database: ")
    for key, value in database.items():
        print(f"Username: {key}\t\t  Password: {value}")

# If user is not admin, create account as long as password has more than 8 characters
else:
    if len(password) > 8:
        database[username] = password
        print(f"\n{username}, you are logged in.")
    else:
        print("\nPassword should have more than 8 characters.")
        quit()

    # Ask if user would like to change password
    choice = input("Would you like to change your password (y/n): ")
    if choice == 'y':
        new_password = input("What would you like your new password to be: ")
        database[username] = new_password
        print(f"{username} your password is now {database[username]}!")
    else:
        quit()




