# 기본적인 for문
# 이터레이션이 가능한 객체를 순차적 순회
# 다른 프로그래밍 언어가 몇 번 반복할지 결정하는 것과 달리 파이썬은 전체 요소를 하나씩 꺼내 동작
# 몇 번 반복할지 정하는 방식으로 프로그램을 구현하려면 range() 함수 사용

# 형식

# for <taget1> in <object>:
# 문장 1
# else:
# 문장 2

# object
# range() 함수 / 문자열 / 리스트/  튜플 / 딕셔너리 / 셋

for x in range(3, 9, 2):  # 3부터 (9-1)까지 2 증가하는 수
    print(x)

for ch in "LOVE":
    print(ch)

ch = [3, 4, 5, 6]

print(*ch, end='')  # end = '' 는 줄바꿈 하지 않는다는 표시!

# table = [["월", "화", "수"], [100, 200, 300]] # 2차원 배열

# print()

# for row in table:
#     for col in row:
#         print(str(col) + "") # col의 타입은 정수, 정수 + 공백 = error / str로 형변환 / 형변환 하기 싫다면 format 사용
#     print()

# lst = ["apple", 100, 3.14]

# for num in lst:
#     print(num, type(num))

# d = {"apple" : 100, "orange" : 200, "banana" : 300}

# for key in d:
#     print(key, d[key]) # value는 방 번호가 되는 것과 같다.

# for k, v in d.items(): # 앞 : 키 / 뒤 : 값 = 키와 값을 한 번에 보는 법
#     print(k, v)

# a = [(1,2), (3,4), (5,6)]

# for (i, j) in a:
#     print(i + j)


# 별을 찍는 세 가지 방법
# for i in range(10):
#     for j in range(i + 1):
#         print("*", end = '')
#     print('')

# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print("*"*i)

# for i in range(1, 11):
#     print("*"*i)

# 구구단 출력
# for i in range(2, 6):
#     for j in range(1, 10):
#         print('{0} x {1} = {2}'.format(i, j, i * j))
#     print()

# for i in range(5):
#     print('  ' * (10 - i) + "* " * (i * 2 + 1))

# table = [["월", "화", "수"], [100, 200, 300]] # 2차원 배열

# print()

# for row in table:
#     for col in row:
#         print(str(col) + "") # col의 타입은 정수, 정수 + 공백 = error / str로 형변환 / 형변환 하기 싫다면 format 사용
#     print()

# for i in range(1, 9 + 1):
#     if i % 2 == 0:
#         break
#     print("2 x {} = {}".format(i, 2 * i))

# array = []
# for i in range(1, 10, 2):
#     array.append(i*i)

# # 한 줄로 단축 가능
# array = [i*i for i in range(1, 10, 2)]
# for i in array:
#     print(i)

# while

# x = 3
# while x < 6:
#     print(x)

# echo = input()
# while echo != "exit":
#     print(echo)
#     echo = input()

# while True:
#     if echo == "exit":
#         break
#     print(echo)
#     echo = input()

# 제어문 관련 유용한 함수

# range() : 규칙 있는 수열 생성, 시작종료증감스텝을 지정하면 수열 생김 <리스트>

# print (list(range(10)))
# print(list(range(10, 0, -1)))

# list = [1,2,3,4,5]
# print(lst)
# lst [i ** 2 for i in lst]

# test = ("apple", "banana", "orange")
# test_len = [len(i) for i in test]
# print(test_len)

# d = {100 : "apple", 200 : "banana", 300 : "orange"}
# d_upper=[v.upper() for v in d.values()]
# print(d_upper)

# lst = [10, 25, 30]
# itel = filter(None, lst)
# for item in lst:
#     print("item:{}".format(item))

# def getBiggerThan(i):
#     return i > 20

# lst = [10, 25 ,30]
# itel = filter(getBiggerThan, lst)
# for item in itel:
#     print("item:{}".format(item))

# i = int(input("숫자 입력 : "))

# if i % 3 == 0:
#     print("{}는 3의 배수이다.".format(i))
# if i % 5 == 0:
#     print("{}는 5의 배수이다.".format(i))
# if i % 8 == 0:
#     print("{}는 8의 배수이다.".format(i))
# if i % 3 != 0 and i % 5 != 0 and i % 8 != 0:
#     print("어느 배수도 아니다.")

# 다다음주 수행 30일
# 시험범위 8~97 + 표준 함수, 사용자 정의 함수 (실습은 하지만 시험에 안 나올 수도) / 105~133
# 함수까지


# 한 직장인의 연간 근로소득 입력받아서 소득세 구하기

# money = int(input("근로소득 입력 : "))

# if money <= 20000000:
#     tax = 0.05
# elif money <= 40000000:
#     tax = 0.15
# elif money <= 80000000:
#     tax = 0.25
# else:
#     tax = 0.4

# sale = int(money * tax)

# print("소득세 : {}".format(sale))

# 연봉과 근무평가 등급 입력, 연봉 인상액, 새연봉 계산 / 단위 만원

money = int(input("현 연봉 입력(단위 : 만 원) :"))
grade = input("근무평가등급 입력 : ")

if grade == "우수":
    up = 0.06
elif grade == "보통":
    up = 0.04
elif grade == "불량":
    up = 0.02

upMoney = money * up
newMoney = money + upMoney

print("****단위 : 만 원****")
print("연봉인상액 : {}".format(upMoney))
print("새 연봉인상액 : {}".format(newMoney))
