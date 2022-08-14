# 2311 최윤영

score = input("점수 입력 : ")

sc = score.split(" ")  # 공백으로 나누기

cnt = [0, 0, 0, 0, 0]  # 5개 입력받기

for s in sc:
    if int(s) >= 90:  # 만약 sc에 입력된 값이 90보다 크거나 작으면
        cnt[0] += 1  # cnt 0번 방에 ++
    elif int(s) >= 80:  # ``
        cnt[1] += 1
    elif int(s) >= 70:
        cnt[2] += 1
    elif int(s) >= 60:
        cnt[3] += 1
    else:
        cnt[4] += 1


print("90점 이상 :" + "\t\t" + '*'*cnt[0])  # 탭 두 번으로 공간 나누고 cnt 0번 방 개수만큼 * 출력
print("80점 대 :" + "\t\t" + '*' * cnt[1])
print("70점 대 :" + "\t\t" + '*' * cnt[2])
print("60점 대 :" + "\t\t" + '*' * cnt[3])
print("60점 미만 :" + "\t\t" + '*' * cnt[4])


print("최고 점수 : ", max(sc))  # 입력된 sc 중 가장 큰 값
print("최저 점수 : ", min(sc))  # 입력된 sc 중 가장 작은 값
