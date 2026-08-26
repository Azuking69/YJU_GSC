# class 정의
class Student:
    # 클래스 멤버 변수
    univ = "YJU"

    # 생성자 -> 반환값X
    # 생성자 주소가 복사할 때니까 반환값이 없음
    def __init__(self, arg_name):
      """Object."""
      self.name = arg_name # 인스턴스 멤버 변수
      """self.univ = "YJU" # 인스턴스 멤버 변수 -> 불필요(안 보임).
      -> Instantiation
      Student() -> () : 생성자 호출."""


# Instance of Student class
std_1 = Student("글시융 1"); std_2 = Student("글시융 2")
print(std_1.univ, std_2.univ)
Student.univ = "영진전문대"
print(std_1.univ, std_2.univ)