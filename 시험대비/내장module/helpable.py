import sys

if len(sys.argv) == 2:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("도움말을 볼 수 있어요")
        sys.exit()

print("안냐세요")
