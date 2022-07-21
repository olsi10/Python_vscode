# 2311 최윤영

def isPrimeNumber(num):
    print("1 ~ N 까지의 소수와 그 갯수를 구하는 프로그램")
    num = int(input("N 입력 : "))

    cnt = 0

    for i in range(2, num + 1):
        if num % i == 0:
            if(num == 1):
                cnt += 1
                print(i)

    print("1부터 {}까지 소수 개수 : {}".format(i, cnt))

isPrimeNumber(100)