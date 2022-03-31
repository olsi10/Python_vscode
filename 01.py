# print('Welocme To', end = '         ')
# print('IT News', end = '  ')
# print('Web Site')

# print()

# import sys

# print('learn python', file = sys.stdout)
# # file = stdout : 기본 출력장치로 출력하다

# # age = 18
# # print(age)

# # age += 2
# # print(age)

# # age -= 1
# # print(age)

# # after_2 = 2
# # print(age + after_2)

# age = 18
# print(age)

# age *= 2
# #38
# print(age)

# age /= 2
# #19.0
# print(age)

# age //= 2
# print(age)
# #9.0

# age %= 6
# print(age)
# #3.0

# age **= 3
# print(age)
# #27.0

# age = 18
# #type(age)

# print(type(age))

# pi = 3.14
# #type(pi)

# print(type(pi))

# x = 10 + 3.14
# #type(x)
# print(type(x))

# print(int(12.7))
# print(int('321'))
# print(float('65.4'))
# print(float('123e4'))
# print(complex(1.23))
# print(complex('1.23+455.6j'))
# print(str(1.23))

# print("Hello"*5)

# a = 2
# b = 1
# s = "구구단 {0} x {1} = {2}".format(a, b, a*b)
# print(s)

# for a in range(2, 10):
#     print('{0}단'.format(a))
#     for b in range(1, 10):
#         print('{0} * {1} = {2:2}'.format(a, b, a*b))

# #############들여쓰기의 중요성
# for a in range(2, 10):
#     print('{0}단'.format(a))
# for b in range(1, 10):
#     print('{0} * {1} = {2:2}'.format(a, b, a*b))

#print('ddd왔나요?')
#print('eee왔나요?')
#print('qqq왔나요?')

#공통적 처리 : print('%s 왔나요?' % name[i]) 사용

###############서식문자

# % 기호 뒤에 자료형을 가리키는 문자 사용

#ex)  정수 출력시

# num = 50
# s = 'my age %d' % num

# print(s)

# #문자열 %s
# # 정수 %d
# # 실수 %f
# # 8진수 %o
# # 16진수 %x
# # 문자표현 %%#

# names = ['kim', 'park', 'lee']
# for name in names:
#     print('my name is %s' % name)

# money = 10000
# s2 = 'give me %d won' % money
# print(s2)

# d = 3.141592
# print('value %f' % d)

# ##########formatting 해야 하는 수가 두 개 이상일 때

# s1 = 'my name is %s age : %d' % ('mirim', 100)
# print(s1)

# age = 78
# money = 20000
# name = 'Jang'
# weight = 63.12
# etc = 'asdf'
# s2 = 'my name is %s, age : %d, weight  : %f, money : %d, etc : %s' % (name, age, weight, money, etc)
# print(s2)

# % 서식 문자를 이용한 문자열 포매팅은 언뜻 보면
# 타입을 정해주기 때문에 정확해 보이지만, 타입을 정해야 하기 때문에
# 불편함도 존해
# 
# 이를 개선하기 위해서 str.format 형식 등장
# 그 이후에 f-string 방법 등장
# 본인의 취향에 맞게, 편리한 방법 사용

#string formatting - 문자열 포매팅
#문자열에서 특정 부분만 바구고 나머지 부분은 일정하다고 할 때
#문자열 포매팅을 이용해서 보기

month = 1

while month <= 12:
     print(f'2020년 {month}월')
     month = month + 1 #증감

#변해야 하는 값이 있느 위치를 포매팅 할 위치를 잡아서 설정