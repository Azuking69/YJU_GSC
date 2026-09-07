class Student:
    id_cnt = 0

    def __init__(self):
        Student.id_cnt += 1
        self.id = Student.id_cnt

std_1 = Student()
std_2 = Student()
print(std_1.id, std_2.id)