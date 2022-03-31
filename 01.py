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

#f-string이란?
#f-string 포매팅은 파이썬 버전 3.6부터 사용할 수 있음
#f-string의 모양은 f와 {}만 알면 됨
#문자열 맨 앞에 f를 붙여주고,
#중괄호 안에 직접 변수 이름이나 출력하고 싶은 것을 바로 넣으면 됨
#f'문자열 {변수} 문자열'

#문자열 맨 앞에 f를 붙이고 출력할 변수, 값을 중괄호 안에 넣습니다.
s = 'coffee'
n = 5
result = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result)

#f-string 왼쪽정렬
s1 = 'left'
result = f'|{s1:<}|'
print(result)

#f-string 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)

#f-string 오른쪽 정렬
s3 = 'right'
result3 = f'|{s3:>10}|'
print(result3)

#f-string에서 중괄호 출력 방법
num = 10
result = f'my age {num}, {{num}}, {{{num}}}'
print(result)

#변수를 표현하려면 {변수}, 중괄호 + 변수 표현하려면 {{num}}

##f-string과 딕셔너리
#딕셔너리는 특정 키에 특정 값을 연결하여 저장하는 자료 구조이다.
#리스트와 비슷하게 사용할 수 있지만 인덱스로 값에 접근하는 것과 달리 키로 값에 접근
#키로는 문자열, 숫자 또는 변경이 불가능한 형식이면 어떤 자료형이든 사용할 수 있다.
d=  {'name' : 'Mirim', 'gender' : 'female', 'age': 18}
result = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result)

