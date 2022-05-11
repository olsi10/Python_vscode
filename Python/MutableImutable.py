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

############################## 0428 ###############################

#mutable 안에 immutable

# 리스트, 딕셔너리 mutable

# print("=" * 50)

# arr1 = [55, 66, [11, 22], 'a', 'b']
# arr2 = [55, 66, [11, 22], 'a', 'b']

# print(f"arr1 : {arr1}\t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2}\t 주소 : {hex(id(arr2))}")

# print()

# print(f"arr1[0] : {arr1[0]} \t주소 : {hex(id(arr1[0]))}")
# print(f"arr2[0] : {arr2[0]} \t주소 : {hex(id(arr2[0]))}")
# print(f"arr1[1] : {arr1[1]} \t주소 : {hex(id(arr1[1]))}")
# print(f"arr2[1] : {arr2[1]} \t주소 : {hex(id(arr2[1]))}")
# print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
# print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")
# print(f"arr1[4] : {arr1[4]} \t주소 : {hex(id(arr1[4]))}")
# print(f"arr2[4] : {arr2[4]} \t주소 : {hex(id(arr2[4]))}")

# print()

# print(f"arr1[2] : {arr1[2]} \t주소 : {hex(id(arr1[2]))}")
# print(f"arr2[2] : {arr2[2]} \t주소 : {hex(id(arr2[2]))}")

# 리스트 내부에 있는 mutable 요소를 보면 arr1[2], arr2[2]에 있는 리스트 [11, 22]는 각각 주소가 다름

# ################################################################################

#얕은 복사 (=) (값이 아닌 주소 참조, 같은 곳을 가리킴)
# arr1 = [1,2,3]
# arr2 = arr1

# print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")

# print()

# # 내용물에 4 추가
# arr1.append(4)

# # arr1과 arr2에 4 추가됨
# print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")

# print("=" * 50)

# arr1 = [4, 5, 6, [2, 4, 8]]
# arr2 = arr1[:] #여기서 복사

# print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")

# print("\n arr2 22추가")

# arr2.append(22)

# print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")

# print(f"arr1[3] : {arr1[3]} \t 주소 : {hex(id(arr1[3]))}")
# print(f"arr2[3] : {arr2[3]} \t 주소 : {hex(id(arr2[3]))}")

# arr1[3].append(99)

# print("arr1[3].append(99)")

# print(f"arr1[3] : {arr1[3]} \t 주소 : {hex(id(arr1[3]))}")
# print(f"arr2[3] : {arr2[3]} \t 주소 : {hex(id(arr2[3]))}")

# print(f"arr1 : {arr1} \t 주소 : {hex(id(arr1))}")
# print(f"arr2 : {arr2} \t 주소 : {hex(id(arr2))}")
# 완전한 깊은 복사도 아니고 완전한 얕은 복사도 아니다. 고로 얕은 복사

# 깊은 복사 같지만 두 내부 리스트가 동일한 곳을 가리키기 때문에 얕은 복사
# [:] mutable 안에 mutable 있을 때 사용

#####################################################################################

# copy 메서드

# = 주소 동일
# [:] 주소 다름, 내부주소 동일

print('=' * 50)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1.copy() # 깊은 복사처럼 보이지만 주소 복사가 안되므로 얕은 복사
print("1. 전체 춮력")
print(f'arr1 :  {arr1}, add : {hex(id(arr1))}')
print(f'arr2 :  {arr2}, add : {hex(id(arr2))}')

print()

arr2.append(22)
print(f'arr1 :  {arr1}, add : {hex(id(arr1))}')
print(f'arr2 :  {arr2}, add : {hex(id(arr2))}')

# 리스트 속 리스트

import copy

print("copy")

print()

arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = copy.copy(arr1)

print("1. 전체 출력")

print()

print(f'arr1 :  {arr1}, add : {hex(id(arr1))}')
print(f'arr2 :  {arr2}, add : {hex(id(arr2))}')

print()

arr2.append(22)
print(f'arr1 :  {arr1}, add : {hex(id(arr1))}')
print(f'arr2 :  {arr2}, add : {hex(id(arr2))}')