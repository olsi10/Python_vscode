# 87p

# 1. 딕셔너리 변수 our_pots에 학생 이름을 키, 갖고 있는 냄비 수 값으로 하여 우리 반 학생의 정보를 저장해보자.

our_pots = {"김비야": 3, "김유진": 4, "박선주": 7, "백선미": 2, "안소영": 6, "양혜원": 1,
            "이혜령": 99, "임재연": 11, "최윤영": 9, "최혜민": 2, "하도연": 3, "하진": 8}

# 2. for문을 이용하여 our_pots에 저장되어 있는 학생 이름 전체를 출력해 보자.

for name in our_pots:
    print(name)

print()

# 3. our_pots에 {학생 이름}의 집에는 {냄비의 수}개의 냄비가 있다. 형식으로 출력해 보자.

for name in our_pots:
    print('{} 집에는 {}개의 냄비가 있다.'.format(name, our_pots[name]))

print()

# 4. our_pots에서 냄비 수가 세 개 이상인 학생의 이름을 모두 출력해 보자

for name in our_pots:
    if our_pots[name] >= 3:
        print(name)

print()

# 5. 처음 세 개 이상인 학생이 나오면 그 학생의 이름만 출력하고 출력을 멈춰보자

for name in our_pots:
    if our_pots[name] >= 3:
        print(name)
        break

# 6. 구구단 2~9단을 출력하는 프로그램을 for문을 이용해서 출력해보자

for i in range(2, 10):
    print('{}단'.format(i))
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i * j))

print()

# 7. 구구단 2~9단을 출력하는 프로그램을 while문을 이용해서 출력해보자

i = 2

while i < 10:
    print('{}단'.format(i))
    j = 1
    while j < 10:
        print('{} * {} = {}'.format(i, j, i * j))
        j += 1
    i += 1

print()

# 8. 6번과 7번의 차이점을 설명해보자.

# while은 증감식이 따로 필요하다. for문보다 코드 이해할 때 시간이 좀 더 오래 걸리는 것 같다.

# 9. 109p 혼자 해보기
# 매개 변수가 없는 함수 star()를 만들어
# *****
# *****
# *****
# 이 결과가 나오게 하자


def star():
    print('*'*5)


star()
star()
star()

# 10. 클래스룸 탑재된 소수구하기

# 입력 받은 수가 소수인지 판별하는 프로그램을 작성하라
# 소수는 어떻게 구할까?
# n이 소수인지 판별하기 위해서는 2부터 n까지의 숫자 중 나누어서 나머지가 0인
# 숫자가 있고 그 숫자가 다르다면 소수가 아니다.
# 만약 나누어 떨어진 숫자가 n과 같다면 그 수는 소수이다.

# n = int(input("숫자 입력 : "))

# for i in range(2, n + 1):
#     if n % i == 0:
#         if(n == 1):
#             print("소수")
#             break
#         else:
#             print("소수가 아님")
#             break

# 89p

# 1. 1~100 홀수 출력
# for i in range(1, 100, +1):
#     if i % 2 == 1:
#         print(i)

# # 2. 100~200까지 3으로 나누어 떨어지는 수를 출력
# for i in range(100, 200, +1):
#     if i % 3 == 0:
#         print(i)

# 3. 소수 구하는 프로그램 (위에 적음!)

# 4. 1~100중 소수가 몇 개인지