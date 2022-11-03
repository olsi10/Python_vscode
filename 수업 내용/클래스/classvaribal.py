class myClass:
    # 클래스 변수
    a_var = 1000

    # 클래스 내 변수
    def a_method(self):
        self.a_var = 5000
        myClass.a_var = 6000

print("[1] 최초 클래스 변수의 초기값 >>> ", myClass.a_var)

myClass.a_var = 3000
print("[2] 클래스 변수의 초기값을 3000으로 변경 >>>", myClass.a_var)

m1 = myClass()
m1.a_method()
print('[3] 클래스 내 메서드 호출을 통해서 변수값 수정 >>> ', myClass.a_var)

print(m1.a_var)

# myClass.a_method() ERROR!!!