# #리스트 : 값의 나열
# #데이터를 모아 놓은 목록 / 순서가 존재하며 여러가지 자료형 담을 수 있음 / 다른 프로그래밍 언어의 배열 대신 사용

#colors = ['red', 'green', 'blue']
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

###리스트 세트 튜플은 다음과 같이 생성자list(), set(), tuple()을 이용해서 서로 변환 가능

# a = set((1,2,3,2)) #tuple -> set
# print(a)
# print(type(a)) #set은 중복되는 수를 제거하기 때문에 2는 잘려서 나옴

# b = list(a) #set -> list
# print(b)
# print(type(b))

# c = tuple(b) #list -> tuple
# print(c)
# print(type(c))

# ###딕셔너리 -> DICTIONARY이지만 DICT로 씀

# d = dict(a = 1, b = 2, d = 3) #키를 통해 값을 찾음
# print(d)
# print(type(d))

# colors = {"apple" : "red", "banana" : "yellow"} # 키 : 값
# print(colors)

# colors["cherry"] = "red"
# print(colors)


# for item in colors.items(): #items에 있는 것들 하나씩 찍기
#     print(item)


# print(colors)
# del colors["cherry"]
# print(colors)
# colors.clear() #완전히 비워지는 것
# print(colors)

# device = {"아이폰" : 5, "아이패드": 10, "윈도우타블렛": 20} #동일한 키가 있다면 그 키의 '값'만 변경함
# device["아이맥"] = 15
# device["아이폰"] = 6
# print(device)
# del device["아이폰"]
# print(device)

# phone = {"kim" : "1111", "Lee" : "2222", "park" : "3333"}
# print(phone.keys())

# print(phone.values())

# print("park" in phone)
# print("moon" in phone)

# p = phone
# print(p)

# d = {"a" : 100, "b" : 200, "c" : 300}

# for key in d.keys():
#     print(key)

# for value in d.values():
#     print(value)

#문자형 숫자형을 제외한 나머지의 대각의 모양과 특징을 하나씩 알아볼 것임

### bool (boolean)

#사용 가능 값 : true, false
#수치를 논리연산자에 사용하는 경우
##0은 False로 간주
##음수를 포함한 다른 값은 모두 True로 간주

#문자열을 논리연산자에 사용하는 경우에도 "만 False로 간주
#값이 없는 상태를 나타내는 None 도 False

# isRight = False
# print(type(isRight))

# print(1 < 2)
# print(1 != 2)
# print(1 == 2)
# print(True and True and False)
# print(True or False or False)

# print("") #false
# print(" ")#true

####################################0421 복습#######################################


#문자열, 튜플, 딕셔너리, 셋을 리스트화 시키는 것

# l = []
# player = ["Messi", 10, True]
# list("Happy")
# list((1125, 2436))
# list({"menu" : "pizza", "price" : 10000})
# list({"사과", "배"})
from re import X


nums = list(range(3))

# nums + [10, 11]
# print(nums)


# nums += [10, 11]
# print(nums)

# #append, extend 차이
# #append (리스트가 안에 통째로 들어감)
# #extend (값만 들어감 (확장))

# nums.append(20)
# print(nums)

# nums.append([30, 31])
# print(nums)

# nums.insert(2, 40)
# print(nums)

# nums.extend([50, 51])
# print(nums)


# #요소 수정
# nums[7] = 60
# print(nums[7]) #[30, 31]



# #요소 삭제
# del nums[2]
# print(nums)

# print(nums.remove(20)) #중복되는 값이 있을 때 앞에 있는 값을 지움

# print(nums.pop())
# #print(nums)

# print(nums.pop(2))
# #print(nums)

# print(nums.append(10))

# nums.clear()
# print(nums)



# #요소 검색
# nums = list(range(3))
# print(nums)

# nums += [100, 10]
# print(nums)

# print(nums[3])


# #값 in 리스트 = 리스트에 값이 있는지 확인
# print(3 in nums) # 3 없어서 False
# print(10 in nums) # 10 있어서 True

# #내림차순 = sort() -> reverse()

# nums.sort()
# print(nums)

# nums.reverse()
# print(nums)

# print(range(3))


#튜플

# 여러개의 값을 리턴할 때 사용

# t = ()
# print(t)

# xy = (2560, 1440)
# print(xy)

# color = 129, 247, 216
# print(color)

# print(xy + color)
# print(xy * 2)

# color = 129, 247, 216 #패킹 = 괄호를 하나로 생략해도 묶어서 대입, 여러 개로 대입할 때도 하나씩 들어감
# red, green, blue = color  #언패킹

# print(red)
# print(green)
# print(blue)
# x, y = 1920, 1080
# print(x)
# print(y)

# x = 2560
# y = 1440
# x, y = y, x

# print(x)
# print(y)

# a = (123, "abc", True, 123)
# print(a[1])
# print(a[2:])
# print(a[:2])

# # 시험문제 예상 a[1] = 2 # 에러!!! 튜플은 값을 변경할 수 없음

# print(a.index("abc")) # 값에 해당하는 인덱스를 가져온다

# print(a.count(123)) # 값에 해당하는 요소를 가져온다

# t = (1,2,3)
# t += (4,) # t += 4 는 오류남
# print(t)




# 딕셔너리 생성
# d = {}
# print(d)

# urls = {"google" : "google.com", 18 : "unesco.org"}
# print(urls)

# # 딕셔너리 요소 추가
# urls["x"] = 2560 # 키 X가 딕셔너리에 없으면 추가
# print(urls)

# # 딕셔너리 요소 수정
# urls["x"] = 1920
# print(urls)

# # 딕셔너리 요소 제거
# del urls["x"]
# urls.pop(18)

# print(urls)

# urls.clear()
# print(urls)

# # 딕셔너리 요소 검색
# urls = {"google" : "google.com", 18 : "unesco.org"}

# print(urls["google"])

# print(urls.get("google"))

# print("google" in urls)
# print("google.com" in urls)
# print("google.com" in urls.values())

# # 딕셔너리 관련 함수
# print(len(urls))

# print(urls.keys())
# print(urls.values())
# print(urls.items())

# 셋 = 중복없는 자료형

# 셋 생성
# game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
# print(game)

# print(set("Funny"))
# print(set([2048, "Tetris", "Cube"]))
# print([2560, 1440])
# print(set({"google" : "google.com", 18 : "unesco.org"}))
# print(set(range(3)))

# # 셋 추가
# game.add("Fifa")
# print(game)

# game.update(("NBA", "MLB"))
# print(game)

# # 셋 제거
# game.remove("LOL")
# print(game)

# 셋 연산

# 교집합
s3 = {3,6,9,12}
s4 = {4,8,12,16}
print(s3 & s4)
print(s3.intersection(s4))

# 합집합
print(s3 | s4)
print(s3.union(s4))

# 차집합
print(s3-s4)
print(s3.difference(s4))

# 대칭 차집합

print(s3 ^ s4)
print(s3.symmetric_difference(s4))

## 다음 수업은 연습문제 복습하기