import random

origin = [0, 0, 0]
strike = 0
ball = 0
cnt = 0

for i in range(0, 3):
    origin[i] = random.randint(0, 10)

    # origin[i] = int(random.random()* 10) # 0 ~~~~~~9. 999 인데 int로 형변환을 하면 0 ~ 9

    # origin[i] = random.choice([0,1,2,3,4,5,6,7,8,9]) # 데이터가 별로 없을 경우에 선택하게 하는 방법도 있음6

    for j in range(0, i):
        while origin[i] == origin[j]:
                origin[i] = random.randint(0, 9) # 같으면 새로 넣어줌

    print(origin[i], end = '')

# user

while(True):
    myData = [0, 0, 0]

    myData = input(' 입력 >>> ').split(' ')
    myData = list(map(int, myData))
    cnt+=1


    # strike
    for i in range(0, 3):
        if (origin[i] == myData[i]):
            strike += 1


    # ball
    for i in range(0, 3):
        for j in range(0, 3):
            if (i != j):                    # i와 j가 다르면서 (i와 j가 같다는 건 이미 스트라이크에서 처리한것) origin의 0방과 myData의 0방이 같을 때
                if origin[i] == myData[j]:
                    ball += 1
                

    print(strike, "strike")
    print(ball, "ball")

    if(strike == 3):
        print(f'축하합니다 {cnt}번 만에 맞춤!')
        break
    elif cnt == 10:
        print('ㅋㅋ 너무 못한당')


# 한 줄로 리스트 입력 받는 법
# l = list(map(int, input().split()))