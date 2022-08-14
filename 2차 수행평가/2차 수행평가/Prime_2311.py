# 2311 최윤영

def isPrimeNumber(n):

    num = int(input("N 입력 : "))  # 숫자 입력
    cnt = 0  # 소수 개수

    for i in range(2, num + 1):  # 2부터 검사 2~num
        b = True  # 모든 수가 소수라고 가정
        for j in range(2, i):  # 2 ~ i - 1 까지 반복
            if i % j == 0:  # num 전까지 나눴으 ㄹ때 나누어 떨어지면
                b = False  # 소수가 아님
                break  # 빠져나가기

        if b is True:  # True로 오면 소수
            print(i, end=" ")  # 줄바꿈 없이 한 줄로 출력
            cnt += 1  # 소수 개수 ++

    print()

    print("1부터 {}까지 소수 개수 : {}".format(num, cnt))

    # 조건 1 매개변수 소수여부 판단
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


isPrimeNumber(100)
