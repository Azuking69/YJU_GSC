class Bar:
    def __init__(self):
        self.name = "GSC"
        self.age = 100 # 새롭게 추가

    def prt_info(self):
        print(self.name, self.age)


class Foo(Bar):
    def __init__(self):
        self.age = 18
        super().__init__()


obj = Foo()
obj.prt_info()