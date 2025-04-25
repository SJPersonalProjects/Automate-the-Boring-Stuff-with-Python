# Printing the list items and its index using enumerate function.

supplies = ["pens", "staplers", "flamethrowers", "binders"]

for index, item in enumerate(supplies):
    print("Index " + str(index) + " in supplies " + item)