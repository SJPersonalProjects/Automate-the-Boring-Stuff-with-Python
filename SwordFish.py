# Shows the usage of infinite while loop
# Uses the continue and break statements.

while True:
    print("Who are you?")
    name = input()
    
    if name != "Sam":
        continue
    print("Hello Sam, What's the password?")
    password = input()
    if password == "SwordFish":
        break
print("Access Granted")
