def spam():
    eggs = "spam local"
    print(eggs)

def becon():
    eggs = "becon local"
    print(eggs)
    spam()
    print(eggs)

eggs = "global"
becon()
print(eggs)