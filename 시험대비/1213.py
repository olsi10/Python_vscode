# def s(para):
#     return para, "힛"


# s("뿡")

# # 파라미터 -> 매개변수 / 아규먼트 -> 함수 호출할 때 같이 보내는 인자

# pi = 3.14152
# print(pi, "의 소수점 1자리 반올림", round(pi))  # 생략할 경우 소수 첫째에서 반올림
# print(pi, "의 소수점 1자리 반올림", round(pi, 0))  # 3.0
# print(pi, "의 소수점 2자리 반올림", round(pi, 1))

# # float -> 문자열 to 실수형
# # int -> 문자열 to 정수형

# st = "1.23"
# fl = 1.23
# i = 5

# print(float(st))  # 1.23
# # print(int(st))  # Error
# str(fl)
# print(type(fl))   # "1.23" 엥ㅇ ㅙ자꾸 float이 나와? 형변환 해ㅡㄴㄴ데
# # 아래처럼 변수에 형변한 값을 넣어야 하나

# # test@@@@@@@@@
# a = "1.2345"
# b = float(a)
# print(b, type(b))  # 1.2345, class <float>

# c = 1.2345
# d = str(c)
# print(d, type(d))  # 1.2345, class <str>
# # test@@@@@@@@@

# len() 리스트 항목 개수
# li = [1, 2, 3, 4, 5, 6, 10, 9, 8, 7]
# print(len(li))      # 개수
# li.sort()           # 정렬
# print(li)           # 정렬

# li = [1, 2, 3, 4, 5, 6, 10, 9, 8, 7]
# li.sort(reverse=True)  # 역정렬
# print(li)

# li = [1, 2, 3, 4, 5, 6, 10, 9, 8, 7]
# li.reverse()        # 뒤집기
# print(li)           # 뒤집기

# li = [1, 2, 3, 4, 5, 6, 10, 9, 8, 7]
# for i, value in enumerate(li):
#     print("인덱스", i, "위치값", value)

# li = ["뿡0", "뿡1", "뿡2", "뿡3", "뿡4", "뿡5"]
# for i, value in enumerate(li):
#     print("index", i, "location", value)

# str = "문자열"
# print(str)
# n = 3
# print(str(n)) # 이름이 1행에서 덮어쓰여져 에러

# 사용자 정의 함수 우선 순위
# def input(s):
#     print(s, "사용자 정의 함수@!")


# a = input("입력 >>>")
# input("얏")

# def minmax(num):
#     a = num[0]
#     b = num[0]
#     for i in num:
#         if a < i: # 최대
#             a = i
#         elif b > i: # 최소
#             b = i

#     return b, a


# min_value, max_value = minmax([3, -16, 1, 12, 31])
# print(f'최솟값 {min_value}, 최댓값 {max_value}')

# def p(s, sn, *args):
#     str = args[0]
#     for i in range(1, len(args)):
#         str = str + (s * sn) + args[i]
#     print(str)


# p(",", 3, 'a', 'b')
# p("_", 3, 'a', 'b', 'c')
# p("ㅜ", 3, 'a', 'b', 'c', 'd')

# str 함수 정의
# def star(s, n):
#     print(s * n)
# # 이런 결과 나오도록
# star("D", 3)  # DDD
# star("A", 5)  # AAAAA

# def sum(*num):
#     sum_value = 0
#     for i in num:
#         sum_value = sum_value + i
#     return sum_value


# result = sum(1, 3)
# print("1 + 3 = ", result)
# print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))

# def min(*num):
#     min_value = num[0]
#     for i in num:
#         if min_value > i:
#             min_value = i
#     return min_value


# result = min(1, 3)
# print("[1, 3] 중 작은 값 = ", result)
# print("[1, 3] 중 작은 값 = ", min(-1, -11, 2, 3, 5, 7))

# def multi(m, start, end):
#     result = []
#     for n in range(start, end):
#         if n % m == 0:
#             result.append(n)
#     return result


# multi2 = multi(17, 1, 100)
# print("mul (17, 1, 100) = ", multi2)
# print()
# multi3 = multi(10, 1, 100)
# print("mul (3, 1, 100) = ", multi3)

# def min_max(*args):
#     min = args[0]
#     max = args[0]

#     for i in args:
#         if min > i:
#             min = i
#         elif max < i:
#             max = i

#     return min, max


# print(min_max(52, -3, 23, 89, -21))
# min_value, max_value = min_max(52, -3, 23, 89, -21)
# print("최저값 : ", min_value)
# print("최고값 : ", max_value)

# 이름을 입력받아 성과 이름을 나누어 리턴하는 함수 div_name
# def div_name(name):
#     name.strip()
#     first_name = name[0]
#     second_name = name[1:]
#     s = "성: " + first_name + "\n" + "이름: " + second_name
#     return s


# myName = input("이름 입력 >>> ")
# print(div_name(myName))

# import random


# def dice_list(pip, repeat):
#     result = []
#     for i in range(1, repeat + 1):
#         dice = random.randint(1, pip)
#         result.append(dice)
#     return result


# result = dice_list(6, 3)
# print("6면 주사위 3번 굴린 결과 : ", result)


# def circle_area(width):
#     radius = width / 2
#     return (radius * radius) * 3.14


# print(circle_area(4))

# def sum_avg(*args):
#     sum_value = 0
#     avg_value = 0
#     arl = len(args)
#     for i in args:
#         sum_value = sum_value + i

#     avg_value = sum_value / arl

#     return sum_value, avg_value


# print(sum_avg(1, 4, 6, 10, 9))
# sum_value, avg_value = sum_avg(1, 4, 6, 10, 9)
# print("합계 : ", sum_value)
# print("평균 : ", avg_value)

# def prime(start, end):
#     result = []
#     for i in range(start, end + 1):
#         if i % 2 == 1:
#             result.append(i)
#     return result


# result = prime(1, 5)
# print("[1, 5] 사이의 소수는? : ", prime(1, 5))

# def login(id, pw):
#     if id == "yo" and pw == "yoo":
#         return True
#     else:
#         return False


# id = input("아이디 입력 >>> ")
# pw = input("비번 입력 >>> ")

# result = login(id, pw)
# print("결과는? ", result)

# def wc(str):
#     str = str.replace(" ", "")
#     return len(str)


# result = wc("y o o")
# print("y o o 공백을 제외한 문자열 개수 >>> ", result)
