# 2311 최윤영

# li = int(input('수를 입력하세요'))


print("수를 입력하세요 : ")

putList = []

def min_in_list(putList):
    # m = putList[0]
    # for i in putList:
    #     if putList[i] < m:
    #         m = putList[i]

    m = min(putList)
    
    return m

put = int(input(""))
putList.append(put)

while put != 0:
    put = int(input(""))
    putList.append(put)

putList.pop()


print("입력 데이터 : ", *putList, end = '')
print()
print("가장 작은 수 : ", min_in_list(putList))