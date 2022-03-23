import random

def splitword(word):
    return list(word)

def lottery(array):
    choice=random.choice(array)
    finalchoice=splitword(choice)
    thefinalchoice2=int(random.choice(finalchoice)) % 4
    print("The result is topic number:",thefinalchoice2+1)


