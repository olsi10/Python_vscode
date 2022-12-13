# import os

import sys

# print("현재 작업 디렉터리는", os.getcwd(), " 입니다.")
# os.system('dir')

print('실행 파일 명 : ', sys.argv[0])
for i in range(1, len(sys.argv)):
    print('옵션', i, ' : ', sys.argv[i])

sys.exit()

# for i in range(1, 100):
#     print('실행 x')
