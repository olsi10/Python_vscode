import random

print('0 이상 1미만 실수', random.random())
print('시작  2.5 이상 끝 10.0 미만 실수', random.uniform(2.5, 10.0))
print('0 이상 끝 10 미만 정수', random.randrange(10))
print('1 이상 끝 7 미만 증가 값이 2인 정수', random.randrange(1, 7, 2))

season = ['spring', 'summer', 'fall', 'winter']

print('리스트에서 1개 값 꺼내오기', random.choice(season))

random.shuffle(season)

print('리스트 순서 섞기', season)

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('리스트 값 중복하지 않고 3개 뽑기', random.sample(sample, 3))