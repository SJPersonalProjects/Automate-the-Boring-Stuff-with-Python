import random

message = ["It's certain",
           "It's decidedly so",
           "Yes, definitely",
           "Reply hazy try again",
           "Ask again later",
           "Concentrate and ask again",
           "My reply is no",
           "Outlook not so good",
           "Very doubtful"]

print(message[random.randint(0, len(message) - 1)])