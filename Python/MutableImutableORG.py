# mutable - 변경되는 객체 (객체 상태 변경 가능)
# imutable - 변경되지 않는 객체 (객체 상태 변경 불가능)

# mutable -> list, set, dict
# imutable -> int, float, tuple, str, bool

# mutable은 값이 변경될 수 있는 객체의 경우 모든 객체를 각각 생성해서 참조
# imutable은 값이 같은 경우 변수에 상관없이 동일한 곳 참조

a = 99
b = 99
c = 99

print("imutable 객체")
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
# 99가 다 같은 메모리를 참조함

print("\nmuable 객체")
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
arr3 = [1, 2, 3]

print(hex(id(arr1)))
print(hex(id(arr2)))
print(hex(id(arr3)))
# 리스트 (mutable)는 값이 변할 수 있다. 각각의 주소 생성해서 참조한다.

# mutable과 imutable의 차이 : mutable은 append()와 같이 값이 자유롭게 바뀔 수 있기에
# 각각의 메모리를 할당해주는 게 관리에 용이하다 판단한 듯

print()


# 얕은 복사와 깊은 복사를 리스트를 이용하여 알아보기
# [:], copy, copy.copy

# 리스트는 mutable하다

# = 를 사용하는 얕은 복사
# 리스트와 복사된 리스트 모두 동일한 주소를 참조, 주소(참조) 복사

# 주소 동일
arr1 = [1, 2, 3]
arr2 = arr1 # 얕은 복사

print(f'arr1 : {arr1}, 주소 : {hex(id(arr1))}')
print(f'arr2 : {arr1}, 주소 : {hex(id(arr2))}')
# arr1 = arr2 의 주소가 같다.

arr1.append(4)

print(f'arr1 : {arr1}, 주소 : {hex(id(arr1))}')
print(f'arr2 : {arr1}, 주소 : {hex(id(arr2))}')
# arr1 = arr2 의 주소가 같다.
# 주소(참조)만 복사한 것이기에 원본의 내용이 바뀌면 같이 바뀐다.

# b 에 a를 할당하면 값이 할당되는 것이 아니라 같은 메모리 주소를 바라본다.
# b를 변경하면 같이 a도 바뀐다.
# mutable한 다른 객체 또한 똑같은 현상이 나타난다.

# [:]을 사용하는 얕은 복사

# mutable 안에 mutable이 들어 있을 때 그 mutable에 대해 얕은 복사 사용
# 다른 주소를 참조해서 그냥 보면 깊은 복사처럼 보이지만 내부 주소는 동일한 주소를 참조하기 때문에
# 얕은 복사이다.

arr1 = [4, 5, 6, [2, 4, 8]] # 2, 4, 8 내부 리스트
arr2 = arr1[:] # 얕은 복사

print(f'arr1 : {arr1}, 주소 : {hex(id(arr1))}')
print(f'arr2 : {arr1}, 주소 : {hex(id(arr2))}')

