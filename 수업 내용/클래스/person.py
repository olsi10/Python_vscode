class Person:
    def creat_info(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("---------------------------------------")
        print("이름 : ", self.name)
        print("나이 : ", self.age)
        print("---------------------------------------")

p1 = Person()
p1.creat_info("홍길동", 20)
p1.print_info()

p2 = Person()
p2.creat_info("강감찬", 80)
p2.print_info()

p3 = Person()
p3.creat_info("을지문덕", 123)
p3.print_info()