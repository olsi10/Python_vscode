## mutable : 변경되는 객체(객체의 상태 변경 가능)
## 종류 : list, set, dictionary

## inmutable : 변경되지 않는 객체(객체 상태 변경 불가)
## 종류 : int, float, str, bool

##얕은 복사, 깊은 복사

# print("imutable 객체")
# a = 99
# b = 99
# c = 99
# d = 99
# e = 99

# print(hex(id(a)))
# print(hex(id(d)))
# print(hex(id(c)))
# print(hex(id(d)))
# print(hex(id(e)))

# print()
# print("mutable 객체")

# arr1 = [1,2,3]
# arr2 = [1,2,3]
# arr3 = [1,2,3]
# arr4 = [1,2,3]

# print(hex(id(arr1)))
# print(hex(id(arr2)))
# print(hex(id(arr3)))
# print(hex(id(arr4)))

#imutable 바뀔 가능성이 있는 메모리는 따로따로 잡자. (관리에 용이하다고판단)

#imutable 객체

# print("=" * 50)
# print("imputable 갹채ㅔ 예제")
# print("=" * 50)
# print("1. int 값이 변경되면?")

# num1 = 99
# num2 = 99
# num3 = 99
# num4 = 99

# print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
# print(f"num1 값 : {num2} \t주소 : {hex(id(num2))}")
# print(f"num1 값 : {num3} \t주소 : {hex(id(num3))}")
# print(f"num1 값 : {num4} \t주소 : {hex(id(num4))}")

# num1 += 1
# num3 += 3
# num4 += 10

# print()

# print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
# print(f"num1 값 : {num2} \t주소 : {hex(id(num2))}")
# print(f"num1 값 : {num3} \t주소 : {hex(id(num3))}")
# print(f"num1 값 : {num4} \t주소 : {hex(id(num4))}")

# print()

# s1 = "Blackdmask"
# s2 = "Blackdmask"
# s3 = "Blackdmask"
# s4 = "Blackdmask"

# print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
# print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
# print(f"s3 값 : {s3} \t주소 : {hex(id(s3))}")
# print(f"s4 값 : {s4} \t주소 : {hex(id(s4))}")

# s1 = s1.replace('D', 'ZZZ') #replace로 값 변경, 새로운 문자열 s1에 대입
# s2 = "BlackZZZMask"         #repalce로 변경한 문자열과 동일한 문자열로 변경
# s4 = s3.upper()             #대문자로 변경
# print()

# print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
# print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
# print(f"s3 값 : {s3} \t주소 : {hex(id(s3))}")
# print(f"s4 값 : {s4} \t주소 : {hex(id(s4))}")

#mutable 객체

# print("=" * 50)
# print("mutable 객체")
# print("=" * 50)
# print("1. List 객체 예제")

# arr1 = ['a', 'b', 77]
# arr2 = ['a', 'b', 77]
# arr3 = ['a', 'b', 77]

# print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
# print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
# print(f"arr3 값 : {arr2} \t주소 : {hex(id(arr3))}")

# arr1.append(10)
# arr2.append(10)

# print()

# print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
# print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
# print(f"arr3 값 : {arr3} \t주소 : {hex(id(arr3))}")


# print("2. dictionary 값이 변경되면?")

# d1 = {'a' : 11, 'b' : 22, 'c' : 33}
# d2 = {'a' : 11, 'b' : 22, 'c' : 33}
# d3 = {'a' : 11, 'b' : 22, 'c' : 33}

# print(f"d1 값 : {d1} \t 주소 : {hex(id(d1))}")
# print(f"d2 값 : {d2} \t 주소 : {hex(id(d2))}")
# print(f"d3 값 : {d3} \t 주소 : {hex(id(d3))}")

# d1['a'] = 99
# d2['d'] = 44

# print()

# print(f"d1 값 : {d1} \t 주소 : {hex(id(d1))}")
# print(f"d2 값 : {d2} \t 주소 : {hex(id(d2))}")
# print(f"d3 값 : {d3} \t 주소 : {hex(id(d3))}")