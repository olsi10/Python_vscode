import calculator as d

a = int(input("첫 번째 수는? "))
b = int(input("두 번째 수는? "))

print(a, " + ", b, " =", d.add(a, b))

print(a, " - ", b, " =", d.sub(a, b))

print(a, " * ", b, " =", d.mul(a, b))

print(a, " / ", b, " =", d.div(a, b))