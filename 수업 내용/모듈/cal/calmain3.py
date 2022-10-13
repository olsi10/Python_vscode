from calculator import *

a = int(input("첫 번째 수는? "))
b = int(input("두 번째 수는? "))

print(a, " + ", b, " =", calculator.add(a, b))

print(a, " - ", b, " =", calculator.sub(a, b))

print(a, " * ", b, " =", calculator.mul(a, b))

print(a, " / ", b, " =", calculator.div(a, b))