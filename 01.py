# print('Welocme To', end = '         ')
# print('IT News', end = '  ')
# print('Web Site')

# print()

# import sys

# print('learn python', file = sys.stdout)
# # file = stdout : 기본 출력장치로 출력하다

# # age = 18
# # print(age)

# # age += 2
# # print(age)

# # age -= 1
# # print(age)

# # after_2 = 2
# # print(age + after_2)

# age = 18
# print(age)

# age *= 2
# #38
# print(age)

# age /= 2
# #19.0
# print(age)

# age //= 2
# print(age)
# #9.0

# age %= 6
# print(age)
# #3.0

# age **= 3
# print(age)
# #27.0

# age = 18
# #type(age)

# print(type(age))

# pi = 3.14
# #type(pi)

# print(type(pi))

# x = 10 + 3.14
# #type(x)
# print(type(x))

# print(int(12.7))
# print(int('321'))
# print(float('65.4'))
# print(float('123e4'))
# print(complex(1.23))
# print(complex('1.23+455.6j'))
# print(str(1.23))

print("Hello"*5)

a = 2
b = 1
s = "구구단 {0} x {1} = {2}".format(a, b, a*b)
print(s)

for a in range(2, 10):
    print('{0}단'.format(a))
    for b in range(1, 10):
        print('{0} * {1} = {2:2}'.format(a, b, a*b))

#들여쓰기의 중요성
for a in range(2, 10):
    print('{0}단'.format(a))
for b in range(1, 10):
    print('{0} * {1} = {2:2}'.format(a, b, a*b))