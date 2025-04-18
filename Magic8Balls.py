import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It's certain"
    elif answerNumber == 2:
        return "It's decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    else :
        return "Very doubtful"
    
randomChoice = random.randint(1, 9)
fortune = getAnswer(randomChoice)
print(fortune)

print("____________________________________________")
print(getAnswer(random.randint(1, 9)))