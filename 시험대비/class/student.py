class Student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade

    def study(self):
        print("공붛다ㅏ")

    def hello(self):
        print("인사하다")


class Leader(Student):
    def __init__(self, name, id, grade):
        super().__init__(name, id, grade)

    def report(self):
        print("조사하다")
