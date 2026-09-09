class Student:
    id_cnt = 0

    def __init__(self):
        Student.inrc_id()
        self.id = Student.id_cnt

    @classmethod
    def inrc_id(cls):
        cls.id_cnt += 1

std_1 = Student()
std_2 = Student()
print(std_1.id, std_2.id)