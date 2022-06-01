# 0601 python 6시간 강의

# 0601 목표 2시간 수강

print(not True) # False

###############연산자

print((3 > 0 ) and (3 < 5)) # True
print((3 > 0) & (3 <5)) # True 

print((3 > 0 ) or (3 < 5)) # True
print((3 > 0) | (3 < 5)) # True

###############간단한 수식

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 * 3 + 4
print(number) # 14
number = number + 2 # 16
number += 2 # 18
number *= 2 # 36
number /= 2 # 18
number -= 2 # 16

number %= 2 # 0

###############숫자 처리함수

print(abs(-5)) #절댓값 5
print(pow(4, 2)) #n승 16
print(max(5, 12)) #최대값 12
print(min(5, 12)) #최소값 5
print(round(3.14)) # 반올림 3
print(round(3.99)) # 반올림 4

from functools import WRAPPER_ASSIGNMENTS
from ipaddress import NetmaskValueError
from math import *
from nturl2path import url2pathname
from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME
from unicodedata import name # math 라이브러리 안에 모든 것을 사용(*)하겠다.

print(floor(4.88)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

# 퀴즈

# 변수를 이용해서 다음 문장을 출력하시오.
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력

# 출력 문장
# XX행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

##############랜덤 함수

from random import * # random 라이브러리 안에 모든 것을 사용하겠다.

print(random()) # 0.0 ~ 1.0 미만 임의값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의값 생성
print(int(random() * 10)) # 0 ~ 10 이하의 소수점이 아닌 정수형 임의값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의값 생성

#############로또 랜덤

print(int(random() * 45) + 1) # 1 ~ 14 이하의 임의갑 생성
print(int(random() * 45) + 1) # 1 ~ 14 이하의 임의갑 생성
print(int(random() * 45) + 1) # 1 ~ 14 이하의 임의갑 생성

# 간결하게 줄이면

print(randrange(1, 46)) # 1 ~ 46 미만의 임의값 생성

# 퀴즈
# # 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회스터디를 하는데 3번은 온라인, 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하세요.

# 조건 1. 랜덤으로 날짜 뽑기
# 조건 2. 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3. 매월 1~3일은 스터디 준비를 해야 하므로 제외

# 출력문 예제
# 오프라인 스터디 모임 날짜는 매월 x일로 선정됐습니다.

from random import *

study = int(random() * 29) + 4
print("오프라인 스터디 모임 날짜는 매월 " + str(study) + "일로 선정되었습니다.")

###########문자열 슬라이스

jumin = "050304-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("생년월일 : " + jumin[:6]) # 처음부터 6 전까지
print("뒷자리 (7자리) : " + jumin[7:]) # 7부터 끝까지
print("뒷자리 (7자리) : " + jumin[-7:])

########################문자열 함수

py = "Python is Amazing"
print(py.lower())
print(py.upper())

print(py[0].islower()) # Fasle
print(py[0].isupper()) # True

print(len(py)) # 17

print(py.replace("Python", "Java")) # 문자 바꾸기 replace("찾는 문자열", "바꿀 문자열")

index = py.index("n") # 몇 번째에 있는지
print(index) # 5

index = py.index("n", index + 1) # 시작 위치부터 +1 된, 즉 두 번째에 있는 거 찾음

print(py.find("n")) # index 와 같지만 다름. find : 원하는 값이 없으면 -1 반환, index : 오류

print(py.count("n")) # n이 총 몇 번 있는지 알려주는 것

##################### 문자열 포맷

print("나는 %d 살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")

# 퀴즈
# 사이트별로 비밀번호를 만들어주는 프로그램
# 예) https://naver.com
# 규칙 1. http:// 부분 제외 -> naver.com
# 규칙 2. 처음 만나는 점(.) 이후 부분 제외 -> naver
# 규칙 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) 생성된 비밀번호 : nav51!

url = "https://naver.com"

replaceURL = url.replace("https://", "")
delDot = replaceURL[:replaceURL.index(".")] # . 전까지 자름
last = delDot[:3] + str(len(delDot)) + str(delDot.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(url, last))

################# 리스트

# subway = [10, 20, 30]

subway = ["유재석", "조세호", "하하"]

# 조세호 몇 번째 칸?
print(subway.index("조세호") + 1)

# 다음 정류장에서 박명수가 탔다?
subway.append("박명수")
print(subway)

# 유재석과 조세호 사이에 정형돈을 넣었다?
subway.insert(1, "정형돈") # 넣을 위치, 넣을 것
print(subway)

# 뒤에서부터 한 명식 꺼내기
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 사람이 몇 명있는지 확인

subway.append("유재석")
print(subway.count("유재석")) # 2

# 정렬도 가능

num_list = [5,2,4,3,1]
num_list.sort() # 12345
print(num_list)

num_list.reverse()
print(num_list) # 54321

# 전부 지우고 싶어

num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용

num_list = [9,8,7,6,5]
# list = ["조세호", 20, True]

# num_list.extend(list) # 합치기
# print(num_list)

################## 사전, 딕셔너리 dict

cabinet = {3 : "유재석", 100 : "김재석"} # 키 3, 값 유재석

print(cabinet[3]) # 키로 검색하면 값 가져올 수 있음
print(cabinet[100])

print(cabinet.get(3)) # 값 가져오는 법

print(3 in cabinet) # True
print(5 in cabinet) # False

# 딕셔너리에 새 키 값 넣기

cabinet["C-20"] = "조세호"
print(cabinet)

# 값 덮어쓰기 가능

cabinet[3] = "김종국"
print(cabinet)

# 값 빼기

del cabinet[3]
print(cabinet)

# 키만 출력

print(cabinet.keys())

# 값만 출력

print(cabinet.values())

# 키, 값 함께 출력

print(cabinet.items())

# 전부 값 빼기

cabinet.clear()
print(cabinet)

############# 튜플

menu = ("돈까스", "치즈까스")
print(menu)
print(menu[0])

# menu.add("생선까스") # 값 변경 불가!!!

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hooby)

# 위 코드를 간결하게 표현할 때 튜플 사용
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

################## set 집합 중복 X, 순서 X

my_set = {1,2,3,3}
print(my_set) # 중복 값 삭제

java = {"유재석", "양세형"}
python = set(["유재석", "박명수"])

# 교집합, java와 python 중복자 출력

print(java & python) # 유재석
print(java.intersection(python)) # 유재석

# 합집합, java와 python 전부 출력

print(java | python)
print(java.union(python))

# 차집합 java는 맞지만 python은 아닌

print(java - python) # 양세형, 박명수
print(java.difference(python))

# python에 추가

python.add("양세형")
print(python)

# java에서 제거

python.remove("유재석")

########### 자료구조 변경

menu1 = {"커피", "우유", "주스"}
print(menu1, type(menu1)) # set

menu1 =  list(menu1)
print(menu1, type(menu1))

menu1 = tuple(menu1)
print(menu1, type(menu1))

menu1 = set(menu1)
print(menu1, type(menu1))

# 퀴즈
# 당신의 학교에서는 파이썬 코딩 대회를 주최합나다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받습니다.

# 추첨 프로그램을 작성하세요.

# 조건 1. 편의상 댓글은 20명이 작성, 아이디는 1~20으로 가정
# 조건 2. 댓글 내용과 상관 없이 무작위로 추첨하되, 중복 불가
# 조건 3. random 모듈의 shufle과 sample 사용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당점차 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) # 섞기
# print(lst)
# print(sample(lst, 1)) # 한 개 아무거나 뽑겠다.

from random import *

# event = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

event = range(1, 21) # 1부터 20까지 type range
event = list(event) # type list

shuffle(event)

winner = sample(event, 4) # 4명 중 1명 치킨, 3명 커피

print("~~✨ 당첨자 발표 ✨~~")
print("치킨 당첨자 : {0}".format(winner[0]))

print("커피 당첨자 : {0}".format(winner[1:]))

print("축하드립니다!!!")

####### 0601 끝