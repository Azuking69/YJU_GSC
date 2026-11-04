from typing import Any, NoReturn, TypedDict, NotRequired, Union, Optional, Literal, Final, Callable
from dataclasses import asdict, dataclass

class Bar:
    dept: str = "gsc"

    __name: str
    __age: int

    def __init__(self, name:str, age:int) -> None:
        self.__name:str = name    # Instance Member Variable
        self.__age:int = age      # Instance Member Variable

obj = Bar("yju", 20)