# 200p
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self, food):
        print(self.name, "가", food, "를 먹는다")
    
    def __str__(self):
        return self.name, "은는", str(self.age), "살이다"

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def work(self):
        print("일하기")

    def get_salary(self):
        print("급료 받기")
        return self.salary

e = Employee("영희", 19, 100)
print(e)
e.eat("밥")
e.work()
r = e.get_salary()
print("급료는", r, "만 원")