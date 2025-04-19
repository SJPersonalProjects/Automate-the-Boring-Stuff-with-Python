def spam():
    global eggs
    eggs = "spam"

def becon():
    eggs = "becon"

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)