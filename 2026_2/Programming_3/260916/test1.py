class Bar:
    def __init__(self):
        self.name = "GSC"

    def prt_info(self):
        print(self.name, self.age)


class Foo(Bar):
    def __init__(self):
        self.age = 18
        super().__init__()


obj = Foo()
obj.prt_info()