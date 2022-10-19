import random


def lotto():
    loto = random.sample(range(1, 45), 6)
    loto.sort()
    return loto


print(lotto())
