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


#문자열, 튜플, 딕셔너리, 셋을 리스트화 시키는 것

# l = []
# player = ["Messi", 10, True]
# list("Happy")
# list((1125, 2436))
# list({"menu" : "pizza", "price" : 10000})
# list({"사과", "배"})
nums = list(range(3))

# print(l)
# print(player)

# nums + [10, 11]
# print(nums)


# nums += [10, 11]
# print(nums)

# print(nums + [10, 11])
# print(nums += [10, 11])


#append, extend 차이
#append (리스트가 안에 통째로 들어감)
#extend (값만 들어감 (확장))

nums.append(20)
print(nums)

nums.append([30, 31])
print(nums)

nums.insert(2, 40)
print(nums)

nums.extend([50, 51])
print(nums)

nums[7] = 60
print(nums[7]) #[30, 31]

del nums[2]
print(nums)

print(nums.remove(20))

nums.pop()
print(nums)

nums.pop(5)
print(nums)

nums.clear()
print(nums)

nums = list(range(3))
print(nums)

nums += [100, 10]
print(nums)

print(nums[3])

for nums in 3:
    print(nums)

for nums in 10:
    print(nums)