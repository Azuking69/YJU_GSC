class Bar:
  id = 1234 # 클래스 멤버 변수

  def __init__(self):
    self.name = "bar" #인스턴수 멤버 변수

obj = Bar()
print(obj.name, Bar.id) # 1234, "bar"