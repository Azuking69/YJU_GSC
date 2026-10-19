from typing import TypedDict


class State(TypedDict):
    name: str = ""
    age: int = 0
    msg: str = ""

    def __init__(self, name: str, bases: tuple[type, ...], dict: dict[str, type], **kwargs: type) -> None:
        super().__init__(name, bases, dict, **kwargs)


bar1: State = {"name": "gsc", "age": 12, "msg": "님 안녕하세요"}
bar2: State = State({"name": "gsc", "age": 12, "msg": "님 안녕하세요"})

print(type(bar2)) # <class '__main__.State'>