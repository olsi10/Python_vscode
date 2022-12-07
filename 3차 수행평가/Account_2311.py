# 2311 최윤영

import random

print('='*50)
print("계좌 관리")
print('='*50)

print("1.계좌 생성" + "\t" + "2. 입금 3. 출금 4. 잔액 조회" + "\t" + '0. 종료')
print('='*50)

bankList = []

class Account:
    def __init__(self, bankNum, m):
        self.bankNum = bankNum
        self.m = m

    def print_bankNum(self, bankNum):
        self.bankNum = bankNum

    def addMoney(self, add):
        self.add = add
    
    def minMoney(self, min):
        self.min = min
    
    def viewAccount(self, bankNum):
        self.bankNum = bankNum

        print(bankNum + '\t\t')

while (1):

    selectMenu = int(input("메뉴 선택 : "))

    if selectMenu == 1:
        randomBank = random.randint(0, 999999999)
        account = Account(randomBank, 0)
        print("계좌번호 ", account.bankNum, "계좌가 생성되었습니다.")

    elif selectMenu == 2:
        inputBank = int(input("계좌번호 입력 : "))
        for i in bankList:
            if inputBank != bankList:
                outMoney = int(input("입금 금액 : "))
            else:
                print("계좌번호", inputBank, "가 존재하지 않습니다.")

    elif selectMenu == 3:
        inputBank = int(input("계좌번호 입력 : "))
        if inputBank != bankList:
                print("계좌번호", inputBank, "가 존재하지 않습니다.")
        else:
            outMoney = int(input("출금 금액 : "))

    elif selectMenu == 4:
        print("="*50)
        print("계좌번호" + '\t\t' + "잔액")
        print("="*50)

        for i in bankList:
            account.viewAccount(bankNum=[i])
                

    elif selectMenu == 0:
        print("프로그램을 종료합니다.")
        break