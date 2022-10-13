# 파이썬의 생성자 __init__ 메소드를 클래스 내부에 정의해야 함

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("---------------------------------------")
        print("이름 : ", self.name)
        print("나이 : ", self.age)
        print("---------------------------------------")

p1 = Person('홍길동', 65)
p1.print_info()

p2 = Person('강감찬', 120)
p2.print_info()

p3 = Person('최윤영', 18)
p3.print_info()