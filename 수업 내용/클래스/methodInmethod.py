class person:
    def a_method(self):
        print("a_method 호출")
    
    def b_method(self):
        self.a_method()
        a_method()

def a_method():
    print("클래스 외부에서 정의된 a_method")

p1 = person()
p1.a_method()
p1.b_method()