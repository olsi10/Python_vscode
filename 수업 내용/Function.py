# def times (a, b):
#     return a * b

# print(times)            # 함수의 주소값
# print(times(10 ,5))     # 함수의 리턴값

# myTimes = times # times의 주소를 가리킴

# def myTimes (a, b):
#     return a * b

# print(times)            # 함수의 주소값 / 함수 카피 가능 같은 주소를 가리킴!
# print(times(10 ,5))     # 함수의 리턴값


# 표준 함수와 사용자 정의 함수
# 컴파일러가 미리 제공

# pi = 3.56789
# print(pi, "의 소수점 1자리 반올림은", round(pi))
# print(pi, "의 소수점 1자리 반올림은", round(pi, 0))
# print(pi, "의 소수점 2자리 반올림은", round(pi, 1))
# print(pi, "의 소수점 3자리 반올림은", round(pi, 2))
# print(pi, "의 소수점 4자리 반올림은", round(pi, 3))

# numbers = [1, 5, -2, 0 ,6]
# print(numbers, "중 가장 큰 값은 : ", max(numbers))
# print(numbers, "중 가장 작은 값은 : ", min(numbers))
# print(numbers, "합계는 : ", sum(numbers))
# print("2의 10승은 :  ", pow(2, 10))

# print(10, "의 절댓값 : ", abs(10))
# print(-10, "의 절댓값 : ", abs(-10))

# print(128, "의 2진수 : ", bin(128))
# print(255, "의 2진수 : ", bin(255))
# print(7, "의 8진수 : ", oct(128))
# print(8, "의 8진수 : ", oct(8))
# print(15, "의 16진수 : ", hex(15))
# print(16, "의 16진수 : ", hex(16))

# user_name = input("이름은?")
# user_age = input("나이는?")

# print(user_name + "님! 나이는 " + str(user_age ) + "세군요!")

# say = "{0}님! 나이는 {1}세군요 {1}세라니 놀라워"

# print(say.format(user_name, user_age))

# pi = "3.14159"
# print("문자열 출력 : ", pi)
# print("실수 변환 출력 : ", float(pi))
# print(float(pi) + 100)

# year = "2018"
# print("올해 년도 : ", year)
# print("100년 뒤는 ", int(year) + 100, "년입니다")
# print("숫자는 문자열로 변환하려면 str()을 이용합니다")
# print("올해는 " + str(year) + "년 입니다")

# list = ['d', 'c', 'a', 'b']
# list.reverse()
# # print("리스트 항목 순서 뒤집기 ", list) reverse 와 같음!!! 주석해도 결과는 같음 중간 과정이 요약된 것
# # list.sort()
# print("리스트 항목 정렬하기 ", list)
# list.sort(reverse=True)
# print("리스트 항목 역정렬하기 ", list)
# for index, value in enumerate(list):
#     print("인덱스", index, "위치의 값은 ", value)

# str = "나는 문자열"
# print(str)
# n = 3
# print(str(n))

# 함수보다 변수가 먼저임!!!

# 사용자 정의 함수


# import random

# # n = random.randint(1, 6)
# # print("결과 ", n)
# # n = random.randint(1, 6)
# # print("결과 ", n)
# # n = random.randint(1, 6)
# # print("결과 ", n)

# def rolling_dice():
#     n = random.randint(1, 6)
#     print("육면 주사위 굴린 결과 : ", n)


# rolling_dice()

# rolling_dice()

# rolling_dice()


# rolling_dice()

# rolling_dice()

# rolling_dice()

# import random

# def rolling_dice(pip):
#     n = random.randint(1, pip)
#     print(pip, "면 주사위 굴린 결과 :", n)

# rolling_dice(4)
# rolling_dice(16)
# rolling_dice(20)

# import random

# def rolling_dice(pip, repeat):
#     for r in range(1, repeat + 1):
#         n = random.randint(1, pip)
#         print(pip, "면 주사위 굴린 결과 :", r, " : ", n)

# rolling_dice(4, 3)
# rolling_dice(16, 2)
# rolling_dice(20, 4)

# def func_sum(i):
#     sum = 0
#     num = i.split()
#     print(num)
#     for n in range(len(num)):
#         sum += int(num[n])
#     return sum

# in_list = input("데이터 입력 : ")
# print("합 : ", func_sum(in_list))

################## 가변 인수

# def p(*s):
#     str = ""
#     for a in s:
#         str += a
#     print(str)

# p("♡")
# p("♡ ♩")
# p("♡ ♩ ♣  ♠")

# def p(space, space_num, *args):
#     str = args[0]
#     for i in range(1, len(args)):
#         str = str + (space * space_num) + args[i]
#     print(str)

# p(", ", 3, "♡ ", "♩ ")
# p("☆ ", 2, "♡ ", "♩ ", "♣ ")
# p("_ ", 3, "♡ ", "♩ ", "♣ ", "♠ ")

# 임의의 개수의 인자를 받는 함수를 가리켜 가변 인자를 사용
# * 기호를 붙히면 이 자리 이후로 여러 개의 파라미터가 붙을 수 있음
# 가변인수는 매개변수 목록 중 가장 마지막에 배치


# 109p 혼자 해 보기

# def star(i, *cnt):
#     for a in cnt:
#         print(a * i)

# star("♬ ", 3)
# star("♡ ", 1, 2, 3) # 2, 3은 가변

# # 다른 방법

# def star(s, *args):
#     for i in range(0, len(args)):
#         print(s * args[i])

# star("♬ ", 3)
# star("♡ ", 1, 2, 3) # 2, 3은 가변

# 키워드 인자를 사용한 함수, 호출한 함수의 매개 변수 순서대로 호출된 함수의 인자 값이 넘겨짐

# 116~117

# def fn(a,b,c,d,e):
#     print(a,b,c,d,e)

# fn(1,2,3,4,5)
# fn(a=1, b=2,c=3,d=4,e=5)
# fn(e=5,d=4,c=3,b=2,a=1)

# g = 1

# def Scope(a):
#     global g # 전역방 하나만 잡음
#     g = 2
#     return g + a

# print(Scope(1))
# print(g)

# # range (주관식) / 시험 문제 교집합

# def func_sum(i):
#     sum = 0
#     num = i.split()
#     print(num)
#     for n in range(len(num)):
#         sum += int(num[n])
#     return sum

# in_list = input("데이터 입력 : ")
# print("합 : ", func_sum(in_list))

# def union(*str):
#     c = []
#     for item in str:
#         for i in item: 
#             if i not in c:
#                 c.append(i)
#     return c
        

# print(union("HAM", "EGG"))
# print(union("HAM", "EGG", "SPAM"))

# def gugudan(dan = 2):
#     for i in range(dan):
#         for j in range(i, 10 + 1):
#             print("{} * {} = {}".format(i, j, i * j))

# gugudan(3)

# def setValue(newValue):
#     x=  newValue

# retValue = setValue(10)
# print(retValue) # None 리턴값 x

# def swap(x, y):
#     return y, x

# print(swap(1, 2)) # 튜플로 리턴한다. 
# retValue = swap(1, 2)
# print(retValue[0], retValue[1]) # 튜플을 빼고 싶다면 이렇게

# def sum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# result = sum(1, 3)
# print("1 + 3 = ", result)
# print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))


# def min(*args):
#     minNum = args[0]
#     for i in args:
#         if minNum > i:
#             minNum = i
#     return minNum

# result = min(1, 3)

# print("min(1, 3) = ", result)
# print("min(0, 3, -11) = ", min(0, 3, -11))

# def min_max(*args):
#     min = args[0]
#     max = args[0]

#     for i in args:
#         if min > i:
#             min = i
#         if max < i:
#             max = i
#     return min, max

# print(min_max(52, -3, 23, 89, -21))

# minV, maxV = min_max(52, -3, 23, 89, -21)

# print("최저값 : ", minV)
# print("최고값 : ", maxV)

# def multi_num(multi, start, end):
#     result = list()
#     for n in range(start, end):
#         if n % multi == 0:
#             result.append(n)
#     return result

# multi2 = multi_num(17, 1, 100)
# print("multi_num(17, 1, 200 : ", multi2)
# print()
# multi3 = multi_num(3, 1, 100)
# print("multi_num(3, 1, 100) : ", multi3)

def div_name(name):
    return name[0], name[1:]
a, b = div_name("최윤영")

print("성 : ", a)
print("이름 : ", b)

# [ 표현식 for 항목 in 리스트 or 튜플 if 조건문 ]

# list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# 리스트 안에서 for 문 사용하기 1
# list = [ num * 3 for num in list ]
# print(list)

h = "  Happy Programming! "

print(len(h))
print(h.rfind("ap")) # 3