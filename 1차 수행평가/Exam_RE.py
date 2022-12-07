# # 1번

# x = int(input('점수 1 입력 : '))
# y = int(input('점수 2 입력 : '))

# if x > y:
#     x, y = y, x

# for i in range(x, y+1):
#     print("{0}단".format(i))
#     for j in range(1, 10):
#         print('{0} * {1} = {2}'.format(i, j , i*j))
#     print("")

# 2번

sum = 0
score = [0,0,0,0,0]

for i in range(5):
    score[i] = input("점수 {0} 입력 : ".format(i + 1))
    sum = sum + int(score[i])

print("입력된 점수 : ", *score, end = '')

print()

print("합계 : %d" % sum)

avg = sum / 5

print("평균 : {0:0.2f}".format(avg))

if avg >= 60:
    print("{0:0.2f}점으로 합격입니다.".format(avg))
else:
    print("{0:0.2f}점으로 불합격입니다.".format(avg))

print("")

# 3번


# product = {"메로나" : [1000, 20], "비비빅" : [700, 3], "바밤바" : [850, 100]}

# while(1):

#     print("1. 신규 상품 등록")
#     print("2. 상품 수정")
#     print("3. 상품 삭제")
#     print("4. 상품 삭제")
#     print("0. 종료")

#     choose = int(input("메뉴 입력 : "))

#     if choose == 0:
#         print("프로그램을 종료합니다.")
#         break

#     elif choose == 1:
#         print("신규 상품 등록 : ")
#         newProduct = input("상품명 입력 : ")
#         newPrice = int(input("가격 입력 :"))
#         newCnt = int(input("수량 입력 : "))

#         product[newProduct] = [newPrice, newCnt] # 상품 추가

#         print()

#         print(" 상품명\t가격\t수량")
#         for key in product.keys():
#             print("{0:<}\t{1:^}\t{2:>}".format(key, product[key][0], product[key][1]))
        
#         print("")

#     elif choose == 2:
#         print("상품 수정 : ")
#         chgProduct = input("상품명 입력 : ")

#         print("1. 가격 수정")
#         print("2. 수량 수정")

#         moreChoose = int(input("메뉴 입력 : "))
        
#         if moreChoose == 1:
#             chgPrice = int(input("가격 입력 : "))

#             product[chgProduct][0] = chgPrice

#             print()

#             print(" 상품명\t가격\t수량")
#             for key in product.keys():
#                 print("{0:<}\t{1:^}\t{2:>}".format(key, product[key][0], product[key][1]))
        
#         elif moreChoose == 2:
#             chgCnt = input("수량 입력 : ")

#             product[chgProduct][1] = chgCnt

#             print()    

#             print(" 상품명\t가격\t수량")
#             for key in product.keys():
#                 print("{0:<}\t{1:^}\t{2:>}".format(key, product[key][0], product[key][1]))
        
#     elif choose == 3:
#         print("3. 상품 삭제")

#         delProduct = input("상품명 입력 : ")
        
#         del product[delProduct]
        
#         print()

#         print(" 상품명\t가격\t수량")
#         for key in product.keys():
#             print("{0:<}\t{1:^}\t{2:>}".format(key, product[key][0], product[key][1]))