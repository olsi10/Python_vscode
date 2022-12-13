import random


def lotto():
    result = random.sample(range(1, 45), 6)
    result.sort()
    return result


print(lotto())
