class A:
    def __init__(self):
        self.name = "A"

    def prt_info(self):
        print(self.name)


class B(A):
    def __init__(self):
        self.name = "B"


class C(A):
    def __init__(self):
        self.name = "C"


class D(B, C):
    def __init__(self):
        self.name = "D"


obj = D()
obj.prt_info()