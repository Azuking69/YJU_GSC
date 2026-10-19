from typing import TypedDict

bar: dict[str, int | str] = {"name": "gsc", "age": 20}
bar = {"name": 20, "age": "gsc"}  # type: ignore

class Foo(TypedDict):
    name: str
    age: int

foo: Foo = {"name": "gsc", "age": 20}
foo = {"name": 20, "age": "gsc"}  # type: ignore

foo[]