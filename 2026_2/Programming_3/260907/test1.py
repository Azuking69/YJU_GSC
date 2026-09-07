class Student:
    univ = "YJU" # 클래스 변수

    def __init__(self, arg_name, arg_id):
        # 인스턴스 멤버 변수
        self.name = arg_name
        self.id = arg_id

std_1 = Student()
std_2 = Student()