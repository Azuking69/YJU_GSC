class Bar:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}"

obj1 = Bar("gsc", 20)
obj2 = Bar("gsc", 30)

print(obj1, obj2)
