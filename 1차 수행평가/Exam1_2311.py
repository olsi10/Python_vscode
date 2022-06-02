# 2311 최윤영

##### 1번

a = int(input("점수1 입력 : "))
b = int(input("점수2 입력 : "))

if a < b:
    for i in range(a, b+1):
        print("{}단".format(i))
        for j in range(1, 9+1):
            print("{} * {} = {}".format(i, j, i*j))
        print("")
else:
    for i in range(b, a+1):
        print("{}단".format(i))
        for j in range(1, 9+1):
            print("{} * {} = {}".format(i, j, i*j))

# # ###################### 2번
# # ######################

# sum = 0

# for i in range(5):
#     num = int(input("점수 {0} 입력 : ".format(i + 1)))
#     sum = sum + num

# score = []

# print(f'입력된 점수 {num[0]},{num[1]},{num[2]},{num[3]},{num[4]} ')

# print('합계 : ', sum)

# avg = sum / 5

# print('평균 : {0:0.2f}'.format(avg)) 

# if avg >= 60:
#     print('{0}점으로 합격입니다.'.format(avg))
# else:
#     print('{0}점으로 불합격입니다.'.format(avg))

###################### 3번
######################

product = {"메로나" : [1000, 20], "비비빅" : [700, 3], "바밤바" : [850, 100]}

print(product)

##### 3-1번

# print('4. 상품 조회')
print(' 상품명\t가격\t수량')

# print(f'{key:<}')


######################
##### 3-2번

print('1. 신규 상품 등록')
newProduct = input('상품명 입력 : ')
newPrice = input('가격 입력 : ')
newNum = input('수량 입력 : ')

product[newProduct]
product[newPrice]
product[newNum]

print(product)

######################
####### 3-3번

print('2. 상품 수정')
setProduct = input('상품명 입력 : ')
setPrice = input('가격 수정 :')
setNum = input('수량 수정 :')

product[setProduct.value] = setPrice
product[setProduct.value] = setNum

print(product)

######################
####### 3-4번

print('3. 상품 삭제')
delProduct = input('상품명 입력 : ')

product.pop(delProduct)

######################
####### 3-6번

