class A:
    def __init__(self):
        pass

    def prt_info(self):
        print("A의 prt_info")


class B(A):
    def __init__(self):
        super().__init__()

    def prt_info(self):
            print("B의 prt_info")

class C(A):
    def __init__(self):
        super().__init__()

    def prt_info(self):
            print("C의 prt_info")


class D(C, B):
    def __init__(self):
        super().__init__()

    def prt_info(self):
            super().prt_info()
            print("D의 prt_info")


obj = D()
obj.prt_info()