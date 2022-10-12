# from multiprocessing.spawn import import_main_path

# from 모듈 이름 import 함수명 문으로 특정 함수나 클래스 임포트하기

# from sys import exit

import sys

while True:
    print("종ㄹ하려면 exit 를 입력하세요.")
    user_input = input("> ")
    if user_input == "exit":
        exit() # sys의 exit 함수를 임포트 했기 때문에 앞에 sys.을 작성하지 않아도 됨