import hello_func
import greeting_func


def main():
    print("insa func module")
    print("__name__ :", __name__)  # 실행하면 __main__ 출력
    hello_func.hello()
    greeting_func.greeting()


main()
