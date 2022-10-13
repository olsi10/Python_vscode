class Car():
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        print(self.type, "객체 생성")


c = Car('스포츠카', 200)
c1 = Car('경차', 300)
c2 = Car('리무진', 100)

# print(c.type) # 스포츠카
# print(c.speed) # 200