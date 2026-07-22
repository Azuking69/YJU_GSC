class Student:
    def __init__(self, name:str):
        self.name = name
    def prt_info(self, msg:str) -> None:
        print(f"{self.name}님 {msg}")

obj = Student("gsc")
obj.age = 20
print(obj.name, obj.age)

obj.prt_info("232323")