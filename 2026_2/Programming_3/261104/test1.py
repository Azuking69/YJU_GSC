from typing import Any, NoReturn, TypedDict, NotRequired, Union, Optional, Literal, Final, Callable, ClassVar
from dataclasses import asdict, dataclass

class Bar():

    def __init__(self) -> None:
        pass

    def __str__(self) -> str: # str(), print()
        return "hello"
    

obj = Bar()
print(obj)