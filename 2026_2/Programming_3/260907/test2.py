class Student:
    c_var = "class member variable"

    def __init__(self):
        self.i_var = "instance member variable"

    def prtInfo(self):
        print(self.c_var, self.i_var)

        self.c_var = "Yeungjin University"


std_1 = Student()
std_1.prtInfo()
print(std_1.c_var)
print(Student.c_var)