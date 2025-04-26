# Copy Module: copy() and deepcopy() functions.

import copy

spam = ["A", "B", "C", "D"]
print(id(spam))

cheese = copy.copy(spam)
print(id(cheese))

cheese[1] = "E"

print(spam)
print(cheese)