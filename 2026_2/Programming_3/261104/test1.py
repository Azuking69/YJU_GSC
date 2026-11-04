from typing import TypedDict, NotRequired, Union, Optional
from dataclasses import asdict, dataclass

bar: int | str | bool = 2
bar: Union[int, str, bool] = 2

def test1(val) -> str | None:
    if val == 0:
        return "test"

def test2(val) -> Optional[str]:
    if val == 0:
        return "test"
