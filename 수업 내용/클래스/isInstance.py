class person:
    pass

class monster:
    pass

p1 = person()
result = isinstance(p1, person)
print('[1] p1 인스턴스는 person 클래스의 인스턴스 객체가 맞나요? ---> ', result)
print('[1] p1 인스턴스는 person 클래스의 인스턴스 객체가 맞나요?', isinstance(p1, person))


result2 = isinstance(p1, monster)
print('[2] p1 인스턴스는 monster 클래스의 인스턴스 객체가 맞나요? ---> ', result2)
print('[2] p1 인스턴스는 monster 클래스의 인스턴스 객체가 맞나요?', isinstance(p1, monster))