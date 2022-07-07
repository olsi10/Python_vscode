# 2311_최윤영

def intersect():
    str1 = set(input("첫 번째 문자열 입력 : "))
    str2 = set(input("두 번째 문자열 입력 : "))

    str = list(str1.intersection(str2))
    str.sort()

    print(str)

    
intersect()
