class Student:
    c_var = "class member variable"

    def __init__(self):
        self.i_var = "instance member variable"

    def prtInfo(self):
        print(self.c_var, self.i_var)


std_1 = Student()
std_1.prtInfo()