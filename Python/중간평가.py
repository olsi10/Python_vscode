residentNum = "881120-1068234"

print('연월일 : ' + residentNum[:6])
print('숫자 :  ' + residentNum[7:])

#print('성별 : ' + residentNum[7]

print()

list = [1, 3, 5, 4, 2]
print('원본 : ', list)
list.sort()
list.reverse()
print('결과 ', list)

print()

str = ['Life', 'is', 'too', 'short']
i = " ".join(str)
print(i)

t = (1,2,3)
t1 = (4 ,)
print(t+t1)

print()

a = {'A' : 90, 'B' : 80, 'C' : 70}
print('원본 딕셔너리 ', a)
b = a.pop('B')
print('B 추출 후 딕셔너리 ', a)
print('추출된 B의 값', b)

print()

