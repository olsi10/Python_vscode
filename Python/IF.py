# a = 10

# if a > 5:
#     print("a가 10입니다.")
#     print("test입니다.")
# else:
#     print("else문입니다.")

# x = int(input()) # 형변환처럼 입력된 타입을 int로 바꿔줌

# print(x)
# print(type(x))

# if x % 2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

# password = input("숫자 입력 : ")

# if password == "암호":
#     print("암호.")
# else:
#     print("암호 아님.")

# money = 1 # True
# if money:
#     print("택시를")
# print("타고")
 #   print("가자")

 # 오류, 마지막 줄에 단독 들여쓰기 불가

# money = 2000
# card = 1 # True
# if money >= 3000 or card:
#      print("택시 타기")
# else:
#     print("걸어가기")

# pocket = ['paper', 'cellphone', 'money', 'card']

# if 'money' in pocket: # if 'money' not in money: print("카드 꺼내")도 가능하다
#     pass
# else:
#     print("카드 꺼내")
# print("수행 완료")

# if 'money' or 'card' in pocket:
#     print("택시")
# else:
#     print("걸어")

# saying = "Life is too short, you need python"

# if "wife" in saying : print("wife")
# elif "pyhton" in saying and "you" not in saying : print("python")
# elif "shirt" not in saying : print("shirt") #출력후 끝
# elif "need" in saying : print("need")
# else : print("none")

###### 0620 조건식

# 거짓 : 정수 계열의 0, 실수 계열의 0, 시퀀스 계열의 (), {}, [], "", None
# 참   : 0이 아니면, 빈 문자열이 아니면 ,빈 객체가 아니면

print(bool(True))
print(bool(False))
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool([]))
print(bool([1,2,3]))

# 파이썬은 if, if elif, if elif elif 를 대체할 switch~case가 없음
# 스위치 예약어 XXXXXXXX 조심!!

while 1:

    num = int(input("숫자 입력 :"))

    if num < 0:
        if num % 2 == 0:
            print("minus / odd")
        else:
            print("minus / even")

    elif num > 0:
        if num % 2 == 0:
            print("positive num / odd")
        else:
            print("positive num / even")