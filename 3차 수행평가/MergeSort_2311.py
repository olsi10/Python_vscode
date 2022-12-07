# 2311 최윤영


Group1 = input('첫 번째 그룹의 데이터 : ')
g1 = Group1.split(" ")[0:5]

Group2 = input('두 번째 그룹의 데이터 : ')
g2 = Group2.split(" ")[0:6]

Group = g1 + g2

Group.sort()

sortGroup = set(Group)

print("병합된 그룹의 데이터 : ", *sortGroup, end = '')