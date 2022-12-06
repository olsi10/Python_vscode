# 리스트 내장 함수

# revere
import random
list = ['a', 'c', 'b', 'd']
list.reverse()
print(list)  # 순서 뒤집기

list = [1, 3, 4, 2]
list.reverse()
print(list)  # 순서 뒤집기

# sort
list = ['a', 'c', 'b', 'd']
list.sort()
print(list)  # 정렬

list = [1, 3, 4, 2]
list.sort()
print(list)  # 정렬

# 내장 함수와 똑같은 이름의 변수 사용
# str = "문자열"
# print(str)
# n = 3
# print(str(n)) # 에러

# 사용자 정의 함수가 내장 함수 이름과 같다면
# 사용자 정의 함수가 우선!!


def input(s):
    print(s)


input("뿡꺆")

# 매개변수가 있는 함수


def rolling_dice(pip, repeat):
    for r in range(1, repeat + 1):
        n = random.randint(1, pip)
        print(pip, "면 굴린 결과 ", r, ":", n)


rolling_dice(6, 1)
rolling_dice(4, 2)

# 함수에서 가변 인수 -> 인수로 할 변수명 앞에 * 붙이기
# 그러면 해당 인수는 리스트가 된다. for문 등을 통해 꺼내면 됨


def p(*args):
    str = ""
    for a in args:
        str = str + a
    print(str)


p("ㅁ")
p("ㅁ", "ㄴ")
p("ㅁ", "ㄴ", "ㄷ")


def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num) + args[i]
    print(str)


p(",", 3, "a", "g")
p("a", 3, "r", "e", "b")

# 115 혼자 해보기


def str(str, *n):
    for i in n:
        print(str * i)


str("a ", 3)
str("a ", 3, 2, 1)
