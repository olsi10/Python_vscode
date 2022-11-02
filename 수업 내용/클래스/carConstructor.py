class Car():
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        print(self.type, "객체 생성")
    
    def move(self):
        print(self.type, "가", str(self.speed), "속도로 움직입니다.")
    
    def speed_up(self, amount):
        self.speed += amount

    def speed_down(self, amount):
        self.speed -= amount


c = Car('스포츠카', 200)
c.speed_up(10)
c.move()
c.speed_down(50)
c.move()

# print(c.type) # 스포츠카
# print(c.speed) # 200

# 실체화 프로그램이 로딩되면서 메모리에 올라가는 것
# 객체를 만들고 메모리 확보 / 클래스는 메모리 확보 x