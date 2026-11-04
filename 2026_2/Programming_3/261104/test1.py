from typing import Any, NoReturn, TypedDict, NotRequired, Union, Optional, Literal, Final, Callable, ClassVar
from dataclasses import asdict, dataclass

class Bar():

    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str: # str(), print()
        return "hello"

    def __getitem__(self, key:str) -> tuple: # obj[key]
        if key == "info":
            return self.__name, self.__age
    

obj = Bar("gsc", 20)
print(obj["info"])