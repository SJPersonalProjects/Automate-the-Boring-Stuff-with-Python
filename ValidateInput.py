# Using String built-in methods to validate user input.

while True:
    print("Enter your age:")
    age = input()

    if age.isdecimal():
        break
    print("Please enter a number for your age:")


while True:
    print("Select a new password (Letters and Numbers only):")
    password = input()

    if password.isalnum():
        break
    print("Passwords can only contain letters and numbers")
    