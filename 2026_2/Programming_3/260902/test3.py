class Student:
    """
    학교 -> 공통
    학과 -> 공통
    이름
    학번
    GPA
    """

    def __init__(self):
        self.name = "홍길동"
        self.id = 1234
        self.gpa = 4.5

    def get_sum(self):
        self.sum = 20 + 30


obj = Student()
print(obj.__dict__)