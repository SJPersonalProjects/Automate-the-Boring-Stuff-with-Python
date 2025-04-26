# Removing values from the list using remove() method.

numbers = [1, 2, 3, 4, 5]
numbers.remove(2)

print(numbers)

# This will throw a ValueError because the value doesn't exist in the list so it can be removed.
# numbers.remove(6)
# print(numbers)


# Removing value using del statement with index.
del numbers[0]

print(numbers)