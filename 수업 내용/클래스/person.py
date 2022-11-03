# 파이썬은 멤버 변수의 개념이 없기 때문에 self 키워드를 사용하여 멤버 변수에게 넣는다 라고 한다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("---------------------------------------")
        print("이름 : ", self.name)
        print("나이 : ", self.age)
        print("---------------------------------------")

p1 = Person("홍길동", 10)
p1.print_info()

p2 = Person("강감찬", 120)
p2.print_info()

p3 = Person("최윤영", 18)
p3.print_info()