from datetime import date, datetime
from xmlrpc.client import DateTime

print('현 재 시 각')
today = datetime.now()
print('today :' , today)
print('연 월 일 :', today.year, today.month, today.day)
print('시 분 초 :', today.hour, today.minute, today.second)
print('요일 :', today.weekday)

print()

print('특정 날짜 객체')
day = datetime(2018, 1, 1, 0, 0, 0)
print('day :', day)
print('2018년부터 지나온 시간 구하기')
print('today - day', today - day)

print()

christmas = datetime(2022, 12, 25, 0, 0, 0)
print('크리스마스까지 남은 시간 >>> ', christmas - today)