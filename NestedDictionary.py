# Nested dictionary and lists practice.

allGuests = {'Alice': {'apple': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apple': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, items):
    newBrought = 0
    for keys, values in guests.items():
        newBrought = newBrought + values.get(items, 0)
    return newBrought

print("Number of things being brought:")
print(" - Apples            " + str(totalBrought(allGuests, 'apple')))
print(" - Cups              " + str(totalBrought(allGuests, 'cups')))
print(" - Cakes             " + str(totalBrought(allGuests, 'cakes')))
print(" - Ham sandwiches    " + str(totalBrought(allGuests, 'ham sandwiches')))
print(" - Apple pies        " + str(totalBrought(allGuests, 'apple pies')))