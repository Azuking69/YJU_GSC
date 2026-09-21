class A:
    def __init__(self):
        pass


class B(A):
    def __init__(self):
        pass


class C(A):
    def __init__(self):
        pass


class D(B, C):
    def __init__(self):
        pass


print(D.mro())