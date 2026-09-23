class A:
    def __init__(self, salary):
        self.__salary = salary

    @property # Decorator -> Getter 설정
    def salary(self): # 가상의 멤버 변수
        return f"급여: {self.__salary}"

    @salary.setter # Setter -> getter의 가상 멤버 변수 이름을 사용
    def salary(self, value): # 메서드 이름 -> Getter 동일하게 설정, setter 설정값이 있음
        if value > 0:
            self.__salary = value

    @salary.deleter # Deleter -> getter의 가상 멤버 변수 이름을 사용
    def salary(self):
        print("Del is invoked")

obj = A(100)
obj.salary = -100
print(obj.salary) 
