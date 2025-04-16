# Shows the usage of while loop and break statement.

name = ''

# Infinite loop.
while True:
    print("Please enter your name")
    name = input()
    # Breaks out of the loop once the name matches.
    if name == 'Sam': break
print("Thank you")