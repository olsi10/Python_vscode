# 2311 최윤영

score = input("점수 입력 : ")

sc = score.split(" ")

cnt = [0, 0, 0, 0, 0]

for s in sc:
    if int(s) >= 90:
        cnt[0] += 1
    elif int(s) >= 80:
        cnt[1] += 1
    elif int(s) >= 70:
        cnt[2] += 1
    elif int(s) >= 60:
        cnt[3] += 1
    else:
        cnt[4] += 1


print("90점 이상 :" + "\t\t" + '*'*cnt[0])
print("80점 대 :" + "\t\t" + '*' * cnt[1])
print("70점 대 :" + "\t\t" + '*' * cnt[2])
print("60점 대 :" + "\t\t" + '*' * cnt[3])
print("60점 미만 :" + "\t\t" + '*' * cnt[4])

for s in sc:
    max_sc = max(s)
    min_sc = min(s)


print("최고 점수 : ", max_sc)
print("최저 점수 : ", min_sc)
