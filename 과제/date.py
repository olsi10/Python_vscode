from datetime import datetime

today = datetime.today()
onWeek = today.weekday()

week = ""

if onWeek == 0:
    week = "월"

elif onWeek == 1:
    week = "화"

elif onWeek == 2:
    week = "수"

elif onWeek == 3:
    week = "목"

elif onWeek == 4:
    week = "금"

elif onWeek == 5:
    week = "토"

elif onWeek == 6:
    week = "일"

print('오늘은 {}년 {}월 {}일 {}요일입니다.'.format(
    today.year, today.month, today.day, week))
