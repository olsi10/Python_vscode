# 2311 최윤영

class Employee():
    def __init__(self, num, name, code):
        self.num = num
        self.name = name
        self.code = code


class Mananger(Employee):
    def __init__(self, managerM):
        self.managerM = managerM

class Temporary(Employee):
    def __init__(self, temporaryM):
        self.temporaryM = temporaryM

class SalesMan(Employee):
    def __init__(self, salesM):
        self.salesM = salesM

# companyNum = input("사번 : ")
# name = input("이름 : ")
# code = input("기본급 코드 (A~E) :")
# money = input("수당 (관리/영업/임시) : ")
# work = int(input("계약 기간 : "))
        
p1 = Employee("MCRM1", "강민준", "B", 30)
p2 = Employee("MCRM4", "민정우", "B", 30)

print("<< 객체 생성 확인 >>")
