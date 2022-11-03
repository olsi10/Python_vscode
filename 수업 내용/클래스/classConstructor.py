class person:
    count_class = 0

    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power
        
        #increat 메서드 호출   
        self.increate()
        


    # 클래스 변수값 1 증가
    def increate(self):
        person.count_class += 1

p1 = person("a", 10, 2)
print('현재 객체 수', person.count_class)

p2 = person("b", 12, 5)
print('현재 객체 수', person.count_class)

p3 = person("c", 13, 4)
print('현재 객체 수', person.count_class)