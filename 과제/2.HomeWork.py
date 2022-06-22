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
