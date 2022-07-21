# 2311 최윤영

grade = []

while True:
    print("0 입력 >>> 종료")
    a = int(input('<학생 점수를 입력하세요.>'))
    grade.append(a)

    if a == 0:
        print('입력을 종료합니다.')
        grade.pop(-1) # 0 지우기
        break

score = []

star = '*'
cnt = 0

for a in grade:
    if 100>= a >=90:
        cnt += 1
    elif 90 > a>=80:
        cnt += 1
    elif 80 > a>=70:
        cnt += 1
    elif 70 > a>=60:
        cnt += 1
    elif 60 > a >= 0:
        cnt += 1


print('\n====================\n')

print("90점 이상 :" + "\t\t" + '*'*cnt)
print("80점 대 :" + "\t\t" + '*' *cnt)
print("70점 대 :" + "\t\t" + '*' *cnt)
print("60점 대 :" + "\t\t" + '*' *cnt)
print("60점 미만 :" + "\t\t" + '*' *cnt)

print("최고 점수 : ", mx)
print("최저 점수 : ", mn)

# for b in range(len(grade)):
#     #문자열의 길이만큼 0부터 시작해서 b에 대입
#     print(grade[b],':',score[b])
#     #b에 대입되는 수의 칸에 있는 리스트를 출력