class A:
    def __init__(self):
        self.name = "A"


class B(A):
    def __init__(self):
        super().__init__()
        self.name = "B"


obj = B()
print(obj.name)  # 출력: B