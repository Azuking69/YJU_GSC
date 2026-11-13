obj1 = {"age": 20, "dept": "gsc"}
obj2 = {"age": 20, "dept": "gsc"}

print(obj1 == obj2)   # True

class Foo: ...
obj3 = Foo()
obj4 = Foo()
print(obj3 == obj4)   # False
# --------------------------------------
class Foo:
    def __init__(self, value) -> None:
        self.value = value
    
obj3 = Foo(3)
obj4 = Foo(3)
print(obj3 == obj4)   # False
# --------------------------------------
class Foo:
    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, r_opd: Foo) -> bool:
        return self.value == r_opd.value
    
obj3 = Foo(3)
obj4 = Foo(3)
print(obj3 == obj4)   # True