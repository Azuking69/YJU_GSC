from typing import Any, TypedDict, NotRequired, Union, Optional
from dataclasses import asdict, dataclass

bar: int | str | bool = 2
bar: Union[int, str, bool] = 2

def test1(val) -> Any:

        return "test"

