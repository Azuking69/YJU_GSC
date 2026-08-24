class Student:
  def __init__(self, arg_name, arg_math, arg_eng) -> None:
    self.name = ""
    self.math = 0
    self.eng = 0
    self.sum = 0
    self.avg = 0
    
  def get_sum(self):
    self.sum = self.math + self.eng
    
  def get_avg(self):
    self.sum = self.sum / 2


# std_1_name = "홍길동"
# std_1_math = 20
# std_1_eng = 10

# std_1_sum = std_1_math + std_1_eng
# std_1_avg = std_1_sum / 2

std_1 = Student("홍길동", 20, 30)
std_2 = Student("김철수", 50, 10)
std_3 = Student("김영희", 30, 70)