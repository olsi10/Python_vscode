# 2311 최윤영


sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
summin = 0

score = []

for i in range(10):
    score = int(input("점수 입력 :"))

    if score[i] >= 90:
        sum1 = sum1 + 1
    elif score[i] >= 70 and score[i] < 90:
        sum2 = sum2 + 1
    elif score[i] >= 60 and score[i] < 70:
        sum3 = sum3 + 1
    elif score[i] >= 50 and score[i] < 60:
        sum4 = sum4 + 1
    else:
        sum5 = sum5 + 1

print("90점 이상 :", '*'*sum1)
print("80점 대 :", '*' *sum2)
print("70점 대 :", '*' *sum3)
print("60점 대 :", '*' *sum4)
print("60점 미만 :", '*' *sum5)

# print("최고 점수 : ", max)
# print("최저 점수 : ", min)