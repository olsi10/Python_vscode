# 기본적인 for문
# 이터레이션이 가능한 객체를 순차적 순회
# 다른 프로그래밍 언어가 몇 번 반복할지 결정하는 것과 달리 파이썬은 전체 요소를 하나씩 꺼내 동작
# 몇 번 반복할지 정하는 방식으로 프로그램을 구현하려면 range() 함수 사용

## 형식

# for <taget1> in <object>:
    # 문장 1
# else:
    # 문장 2

# object
# range() 함수 / 문자열 / 리스트/  튜플 / 딕셔너리 / 셋

for x in range(3, 9, 2): # 3부터 (9-1)까지 2 증가하는 수
    print(x)

for ch in "LOVE":
    print(ch)

ch = [3, 4, 5, 6]

print(*ch, end = '') # end = '' 는 줄바꿈 하지 않는다는 표시!