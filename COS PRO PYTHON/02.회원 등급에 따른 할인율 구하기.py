# 쇼핑몰에서 회원 등급에 따라 할인 서비스를 제공한다
# "S" = 5% / "G" = 10% / "V" = 15%

# 함수 구현

def solution(grade, price):

    answer = 0

    if grade == "S":
        answer = price - (price * 0.05)
    elif grade == "G":
        answer = price - (price * 0.1)
    elif grade == "V":
        answer = price - (price * 0.15)

    return answer


ret = solution("S", 50000)
ret1 = solution("G", 30000)
ret2 = solution("V", 45000)

print(ret)
print(ret1)
print(ret2)
