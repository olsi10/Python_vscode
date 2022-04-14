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

# month = 1

# while month <= 12:
#      print(f'2020년 {month}월')
#      month = month + 1 #증감

# #변해야 하는 값이 있느 위치를 포매팅 할 위치를 잡아서 설정

# #f-string이란?
# #f-string 포매팅은 파이썬 버전 3.6부터 사용할 수 있음
# #f-string의 모양은 f와 {}만 알면 됨
# #문자열 맨 앞에 f를 붙여주고,
# #중괄호 안에 직접 변수 이름이나 출력하고 싶은 것을 바로 넣으면 됨
# #f'문자열 {변수} 문자열'

# #문자열 맨 앞에 f를 붙이고 출력할 변수, 값을 중괄호 안에 넣습니다.
# s = 'coffee'
# n = 5
# result = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
# print(result)

# #f-string 왼쪽정렬
# s1 = 'left'
# result = f'|{s1:<}|'
# print(result)

# #f-string 가운데 정렬
# s2 = 'mid'
# result2 = f'|{s2:^10}|'
# print(result2)

# #f-string 오른쪽 정렬
# s3 = 'right'
# result3 = f'|{s3:>10}|'
# print(result3)

# #f-string에서 중괄호 출력 방법
# num = 10
# result = f'my age {num}, {{num}}, {{{num}}}'
# print(result)

#변수를 표현하려면 {변수}, 중괄호 + 변수 표현하려면 {{num}}

##f-string과 딕셔너리
#딕셔너리는 특정 키에 특정 값을 연결하여 저장하는 자료 구조이다.
#리스트와 비슷하게 사용할 수 있지만 인덱스로 값에 접근하는 것과 달리 키로 값에 접근
#키로는 문자열, 숫자 또는 변경이 불가능한 형식이면 어떤 자료형이든 사용할 수 있다.
# d=  {'name' : 'Mirim', 'gender' : 'female', 'age': 18}
# result = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
# print(result)

# #f-string과 리스트
# n = [100, 200, 300]
# print(f'list : {n[0]}, {n[1]}, {n[2]}')

# for v in n:
#     print(f'list with for : {v}')

#리스트는 리스트 변수명을 사용하고 리스트 개수만큼 돌림
#인덱스 값처럼 돌아감. 생산성 부분에서는 좋다. 문장의 단순화

######################format 끝#########################################

##변수와 함수 소개

#변수
#프로그래밍 작업을 할 때 기본적으로 변수 함수 필요
#변수 : 값을 저장하기 위한 공간. 저장된 것은 변할 수 있다.
#프로그램을 작성하면서 변수에 임의의 값을 담거나 함수가 리턴하는 값을 저장

# srtA = "Hello python"

#함수
#종류 : 필요한 기능이 미리 구현되어 있는 빌트인 함수 / 사용자가 직접 정의한 함수
#API(Application Programming Interface)
#len()이라는 내장 함수를 입력 파라메터(입력 데이터)로 넘겨진 문자열의 길이를 리턴한다

# strB = "파이썬 연습"
# print(len(strB))
#6자리인 것을 보면 유니코드 사용

#변수명
#대소문자 구분 Freind와 friend는 다른 변수
#코딩을 할 때 대소문자 일치 확인필요
#비주얼 베이직 같은 언어는 구별 x c계열 언어는 구분

#숫자형
#int, float 같은 형식

#문자열형식
#"데이터", "전우치"로 초기화
#문자열 데이터는 반드시 ""나 "로 묶어야 함
#파이썬에서는 ""와 "를 구분하지 않음

#불린형식
#Ture, False 사용 (대문자로 시작)

#파이썬키워드
#파이썬 언어에서 제공되는 기본적인 문장
#미리 정의되어 있는 단어
#변수명이나 함수명으로 사용불가
#파이썬 키워드는 대략 35개
#####키워드는 서치해서 찾아보기####

# import keyword
# print(keyword.kwlist)

#자료형
#숫자형 정수 실수
#문자열 문자들의 모음
#리스트 순서를 가지는 파이썬의 임의 객체 집합 [] 사용
#사전   순서를 가지지 않는 객체의 집합, 키로 값을 꺼낸다. {} 사용
#튜플   순서를 가지는 파이썬의 임의 객체 집합으로 내용 변경이 안됨 ()
#세트   순서를 가지지 않는 유일한 값의 집합형태로 사용, 합집합, 교집합, 차집합을 구할 경우 사용 {}1



#클래스 안에 정의된 것 -> 메소드

#type
# strA = "Hello python"
# x = 5
# y = 3.14

# print(type(strA))
# print(type(x))
# print(type(y))

#
# \n 줄바꿈
# \t 탭
# \r 캐리지 반환
# \0 널
# \\ \문자
# \' 단일부호
# \" 부호

# print("py""thon")
# print("py" + "thon")
# print("py"*3)

# strA = "python"
# print(strA[0])

# #0부터 시작하고 끝부분에서는 자기번호 제외
# print(strA[0:1]) #1까지 나옴
# print(strA[1:3]) #yt
# print(strA[:2])
# print(strA[-2:])
# print(strA[:])

# str8 = "python is powerful"
# # print(str8[0])
# # print(str8[0:8])
# # print(str8[:6])

# # print(str8[-1])
# # print(str8[-2])
# # print(str8[-3:1])
# # print(str8[-8:])

# # print(str8[::2])
# # #시작, 끝 간격 두 칸씩 띄고 출력
# # print(str8[7:18])

# # print(str8[-11:9])
# # print(str8[-18:10])

# #리스트 : 값의 나열
# #데이터를 모아 놓은 목록 / 순서가 존재하며 여러가지 자료형 담을 수 있음 / 다른 프로그래밍 언어의 배열 대신 사용

colors = ['red', 'green', 'blue']
#print(colors)
#print(type(colors))
#type list

#append (요소의 추가) = 기존 리스트에 값을 추가 = 제일 끝으로 들어감

#print(colors)
# colors.append("blue")
# #print(colors)

# #insert = 원하는 위치에 추가

# #print(colors)
# colors.insert(1, 'black') #nnnn.insert(들어갈 자리, 추가할 요소)
# #print(colors)

# #index = 어떤 값이 어디에 있는지 확인 (append 와 동일)

# #2번재 인자를 지정하지 않으면 처음부터 검색, 지정하면 지정된 방 번호 이후의 아이템 방 번호 리턴

# #print(colors)                 
# #print(colors.index("red"))      
# colors+= ["red"]               
# #print(colors)                   
# #print(colors.index("red", 1))
# colors+= "red"
# #print(colors)

# #리스트 메서드 - count() 현재 해당 값 개수를 반환, pop() 값을 뽑아내서 반환

# print(colors)
# print(colors.count("red"))
# print(colors.pop()) #d 아웃
# print(colors.pop()) #e 아웃
# print(colors.pop(1))#black 아웃
# print(colors)
# print()

# #리스트 메서드 - remove() 단순히 해당 값을 삭제, extend() 데이터 추가

# print(colors)
# print(colors.remove("red")) #remove는 프린트 x (none 나옴) 제거한 값 되돌리기 = pop, 그냥 제거하고 싶다면 remove
# colors.remove("red")
# print(colors)

# print()

# print(colors)
# colors.extend(["blue", "yellow", "white"])
# print(colors)

# print(colors.extend(["blue"])) # none 출력

# #리스트 메서드 - sort() 오름차순 정렬, reverse() 내림차순 정렬

# print(colors)

# print()

# colors.sort()
# print(colors)

# print()

# colors.reverse()
# print(colors)

# tuple 튜플
#리스트와 유사 : 순서가 존재
#리스트와 달리 [] 대신 ()로 묶어서 표현하며 읽기 전용
#제공되는 함수는 리스트에 비해적지만 속도는 그만큼 빠르다
#튜플은 일반적인 경우에 데이터를 묶어서 한번에 전달하거나 여러 개의 값을 묶어서 한번에 반환할 경우에 사용됩니다.
#자동 완성 기능을 통해서 보면 시레 제공되는 메서드가 count(), index() 정도만 제공됨

# set(세트) union, intersection, difference
# 수학시간에 배운 집합과 동일
# 유일한 값의 모임이며 순서는 없다

#set
# a = {1,2,3,4}
# b = {3,4,4,5}

#tuple
# #a= (1,2,3)
# #print(type(a))

# #중복되는 값 삭제

# print(a)
# print(b)
# print(type(a))
# print(type(b))

# print()

# print(a.union(b))             #합
# print(a.intersection(b))      #교
# print(a.difference(b))        #차

#-4/14-----------------------------------------------------------------------------------------------------

#튜플이 주로 사용되는 경우 - 함수에서 하나 이상의 값을 리턴하는 경우
# def calc (a, b):
#     return a + b, a* b

# x, y= calc(5, 4)
# print(x, y)

# def num(a, b, c):
#     return a+b, a-b, a*c

# x, y, z = num(2, 4, 5)
# print(x, y, z)

# #print("id : %s, name : %s" % ("kim", "김유신"))

# args = (3, 4)
# print(calc(*args))
# # * -> 포인터 기능

# args2 = (4, 5, 10)
# print(num(*args2))


# set
# a = {1,2,3,4}
# b = {3,4,4,5}

# #중복되는 값 삭제

# print(a)
# print(b)
# print(type(a))
# print(type(b))

# print()

# print(a.union(b))             #합
# print(a.intersection(b))      #교
# print(a.difference(b))        #차

# #결과는 똑같음, 합교차를 기호로
# print(a | b)
# print(a & b)
# print(a- b)

#리스트 세트 튜플은 다음과 같이 생성자list(), set(), tuple()을 이용해서 서로 변환 가능

a = set((1,2,3))
print(a)
print(type(a))