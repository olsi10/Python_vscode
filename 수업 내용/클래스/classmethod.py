class Car:
    count = 0
    
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    # 클래스 변수를 클래스 메소드 안에서 사용할 때 cls 라고 써야함

print(Car.get_count())
c1 = Car("스포츠카", 100)
c2 = Car("경차", 50)
print(Car.get_count())