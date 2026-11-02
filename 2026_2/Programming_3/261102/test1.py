from typing import TypedDict, NotRequired
from dataclasses import asdict, dataclass

@dataclass
class Bar:
    name: str = "gsc"
    age:  int =  10


obj: Bar = Bar(name="yju")
print(obj, type(obj))
print(asdict(obj))

test = {"name": "yju gsc", "age": 20}
obj2: Bar = Bar(**test)
print(obj2)