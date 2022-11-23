# 시작 날짜와 끝 날짜가 구해질 때 두 날짜가 며칠만큼 떨어져 있는지 구하기
# 윤년 고려 X

# 빈칸 채우기

def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0

    for i in range(month-1):
        total += month_list[i]
    total += day

    return total - 1


def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total


ret = solution(1, 31, 2, 2)
print(ret)
