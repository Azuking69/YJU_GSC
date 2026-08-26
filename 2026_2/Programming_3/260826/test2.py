# class 정의
class Student:
  # 생성자 -> 반환값X
  # 생성자 주소가 복사할 때니까 반환값이 없음
  def __init__(self, arg_name):
    # Object
    self.name = arg_name
    # -> Instantiation
    # Student() -> () : 생성자 호출
  

bar = Student("글시융")
print(bar.name)