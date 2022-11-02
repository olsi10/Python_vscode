class Pet:
    # 짖다
    # 어느 한 부분에서 특정적으로 실행되는 객체 = 인스턴스
    # 반드시 첫 번째 매개변수가 주어저야 한다. 대부분 self 사용. 클래스 메서드는 반드시 self라는 첫 번ㅉㅐ 매개변수
    # self가 매개변수다 -> 객체 메서드, 인스턴스 메서드다
    def bark_dog(self):
        print("왈왈~")
    def bark_cat(self):
        print("야용~")
    def bark_mouse(self):
        print("쮴쮴쮞")


# java = Pet p1 = new Pet()
# 파이 = p1 = Pet()

p1 = Pet()
p1.bark_dog()

p2 = Pet()
p2.bark_cat()
p2.bark_dog()

p3 = Pet()
p3.bark_dog()
p3.bark_cat()
p3.bark_mouse()