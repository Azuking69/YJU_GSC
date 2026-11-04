from typing import Any, NoReturn, TypedDict, NotRequired, Union, Optional, Literal, Final, Callable
from dataclasses import asdict, dataclass

class Bar:
    dept: str = "gsc"

    def __init__(self, name:str, age:int) -> None:
        self.__name:str = name        # Instance Member Variable
        self.__age:int = age          # Instance Member Variable
        self.__email:str = "dfdfsf"

obj = Bar("yju", 20)