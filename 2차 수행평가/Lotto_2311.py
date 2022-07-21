# 2311_최윤영

import random


def func_lotto():
    s = set()
    cnt = 0

    while True:
        s.add(random.randint(1, 45))

        if len(s) == cnt + 1:
            cnt += 1

        if cnt == 6:
            break

    return list(s)


for i in range(1, 10 + 1):
    result = func_lotto()

    result.sort()

    print("당첨 번호 : ", end="")

    for num in result:
        print(num, "", end="")

    print()
