# Birthday program to understand dictionaries.

birthdays = {'Alice': 'April 1', 'Bob': 'December 12', 'Carol': 'March 3'}

while True:
    print("Enter a name: (blank to quit)")

    name = input()
    if name == "": break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else :
        print("I don't have birthday information for " + name)
        print("What is their birthday?")

        newBirthday = input()
        birthdays[name] = newBirthday

        print("Birthday database updated")