class Student:
    univ = "YJU" # 클래스 변수

    def __init__(self, arg_name, arg_id):
        # 인스턴스 멤버 변수
        self.name = arg_name
        self.id = arg_id

std_1 = Student("a", 1)
std_2 = Student("b", 2)

print(std_1.id, std_1.name, std_1.univ)
print(std_2.id, std_2.name, std_2.univ)