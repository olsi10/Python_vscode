# 2311_최윤영

import random

num = []

def func_lotto():
    
    while len(num) < 6:
        a = random.randint(1, 45)
        if a not in num:
            num.append(a)
    
    num.sort()

    print(num)

    # n.reverse()

func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()