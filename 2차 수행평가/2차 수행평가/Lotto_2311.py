# 2311_최윤영

import random


def func_lotto():
    s = set()  # 중복 없도록
    cnt = 0

    while True:
        s.add(random.randint(1, 45))  # 1 ~ 45

        if len(s) == cnt + 1:  # 로또 번호의 길이가 1일 때
            cnt += 1  # cnt++

        if cnt == 6:  # 로또 번호의 길이가 6이면
            break  # 멈춰!!

    return list(s)  # 리스트로 변환하기 >>> 오름차순 해야 해서


for i in range(1, 11):  # 1부터 10까지
    result = func_lotto()  # result에 func_loto() 리턴값 대입

    result.sort()  # 오름차순 정렬

    print("당첨 번호 : ", end="")  # 줄바꿈 없이 출력

    for num in result:
        print(num, "", end="")  # 줄바꿈 없이 reuslt 인덱스 하나씩 뽑아내기

    print()  # 줄바꿈
