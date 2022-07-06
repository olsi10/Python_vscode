# 2311 최윤영

def isPrimeNumber(num):
    cnt = 0
    print("1 ~ N 까지의 소수와 그 갯수를 구하는 프로그램")
    num = int(input("N 입력 : "))
    for i in range(2, num):
        if num % i == 1:
            print(i)
            cnt = cnt + 1

        
    print("1부터 {}까지 소수 개수 : ".format(num), cnt)

isPrimeNumber(100)
