from random import shuffle

def to_marry(boys, girls):
    shuffle(boys)
    shuffle(girls)
    marriage = []
    for i in range(min(len(boys), len(girls))):
        marriage.append((boys[i], girls[i]))
    return marriage

# -------------- TEST -------------- #
boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]
print(to_marry(boys, girls))
