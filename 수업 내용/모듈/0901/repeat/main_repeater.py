# import repeater

# from repeater import repeat, once

# 편리하긴 하나 모듈 간 함수가 겹치는 등의 문제 발생
# from repeater import *

# 모듈 이름을 쉽게 바꾸거나 다른 변수와 이름이 겹친다면 import as 구문으로 이름을 변경해서 사용 가능
import repeat as once, repeat


s = input("반복한 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")

repeat(s, int(n))
repeat(s)
once(s)