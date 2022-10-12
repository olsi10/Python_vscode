import random

random_numer = random.randint(1, 100)
print(random_numer)

cnt = 1

while True:
    try:
        num = int(input('1 ~ 100사이의 숫자 입력 : '))
        if(random_numer > num):
            print('Up!!')
        elif(random_numer < num):
            print('Down!!')
        else:
            print('{0}번 시도 끝에... 정답!!!'.format(cnt))
            break
        cnt += 1
    except:
        print('에러 발생')