def s(para):
    return para, "힛"


s("뿡")

# 파라미터 -> 매개변수 / 아규먼트 -> 함수 호출할 때 같이 보내는 인자

pi = 3.14152
print(pi, "의 소수점 1자리 반올림", round(pi))  # 생략할 경우 소수 첫째에서 반올림
print(pi, "의 소수점 1자리 반올림", round(pi, 0))  # 3.0
print(pi, "의 소수점 2자리 반올림", round(pi, 1))

# float -> 문자열 to 실수형
# int -> 문자열 to 정수형

st = "1.23"
fl = 1.23
i = 5

print(float(st))  # 1.23
# print(int(st))  # Error
str(fl)
print(type(fl))   # "1.23" 엥ㅇ ㅙ자꾸 float이 나와? 형변환 해ㅡㄴㄴ데
# 아래처럼 변수에 형변한 값을 넣어야 하나

# test@@@@@@@@@
a = "1.2345"
b = float(a)
print(b, type(b))  # 1.2345, class <float>

c = 1.2345
d = str(c)
print(d, type(d))  # 1.2345, class <str>
# test@@@@@@@@@
