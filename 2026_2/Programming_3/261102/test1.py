from typing import TypedDict


class Bar(TypedDict):
    name: str
    age: int


obj1: Bar = Bar(name = "gsc", age = 20)
obj2: Bar = {"name": "yju", "age":30}

print(obj2, type(obj1))