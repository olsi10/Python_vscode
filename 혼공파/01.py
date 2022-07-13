# pi = 3.141592
# print(pi)


# pi = pi + 2
# print(pi)

# pi = pi * 2
# print(pi)

# pi = pi - 2
# print(pi)

# pi = pi / 2
# print(pi)

# pi = pi ** 2
# print(pi)

# 원에 둘레, 넓이 구하기

# pi = 3.141592
# r = 10  # 반지름

# print("원주율 : ", pi)
# print("반지름 : ", r)
# print("둘레 : ", 2 * pi * r)
# print("넓이 : ", pi * r * r)


str_input = input("태어난 해 입력 >>>")
birth_year = int(str_input) % 12

if birth_year == 0:
    print("원숭이 띠입니다.")
elif birth_year == 1:
    print("닭 띠입니다.")
elif birth_year == 2:
    print("개 띠입니다.")
elif birth_year == 3:
    print("돼지 띠입니다.")
elif birth_year == 4:
    print("쥐 띠입니다.")
elif birth_year == 5:
    print("소 띠입니다.")
elif birth_year == 6:
    print("범 띠입니다.")
elif birth_year == 7:
    print("토끼 띠입니다.")
elif birth_year == 8:
    print("용 띠입니다.")
elif birth_year == 9:
    print("뱀 띠입니다.")
elif birth_year == 10:
    print("말 띠입니다.")
elif birth_year == 11:
    print("양 띠입니다.")
