def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

print("_____________________________________")

# OR.

def divide(divideBy):
    return 42 / divideBy

try:
    print(divide(2))
    print(divide(12))
    print(divide(0))
    print(divide(1))
except ZeroDivisionError:
    print("Error: Invalid argument.")