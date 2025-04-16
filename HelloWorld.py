# This program says "Hello" and asks for my name!

print("Hello, World!")

# Asks for name.
print("What's your name?")
myName = input()

print("It's good to meet ya, " + myName)
print("The length of your name is ", len(myName))
print("The length of your name is " + str(len(myName)))

# Asks for age.
print("What's your age?")
myAge = input()

print("You'll be " + str(int(myAge) + 1) + " in a year.")

# Converting types.

print() # Just for a gap.
print(str(0))