from typing import Any, NoReturn, TypedDict, NotRequired, Union, Optional, Literal, Final, Callable, ClassVar
from dataclasses import asdict, dataclass

class Bar:
    dept: str = "gsc"
    univ: ClassVar[str] = "yju"

    def __init__(self, name:str, age:int) -> None:
        self.__name:str = name        # Instance Member Variable
        self.__age:int = age          # Instance Member Variable

obj = Bar(name="kim", age=20)

obj.dept = "dfsdfsdfsd"
print(Bar.dept)
print(obj.dept)
# obj.univ = "fdsfsdfsdf"