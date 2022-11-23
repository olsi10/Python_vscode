# 학생별로 원하는 티셔츠 사이즈 조사를 했다.
# 순서대로 "XS", "S", "M" "L", "XL", "XXL"
# 조사 결과가 있는 shirt_size 리스트가 매개변수로 주어질 때
# 사이즈별로 티셔츠가 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 return

# 함수 구현

def solution(shirt_size):
    answer = [0, 0, 0, 0, 0, 0]

    for size in shirt_size:

        if size == "XS":
            answer[0] += 1
        elif size == "S":
            answer[1] += 1
        elif size == "M":
            answer[2] += 1
        elif size == "L":
            answer[3] += 1
        elif size == "XL":
            answer[4] += 1
        elif size == "XXL":
            answer[5] += 1

    return answer


shirt_size = ["XS", "S", "XXL", "L", "L", "XS", "XL"]
ret = solution(shirt_size)
print(ret)
