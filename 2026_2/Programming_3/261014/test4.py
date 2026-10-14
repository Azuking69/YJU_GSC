from typing import Optional

bar: Optional[int] = None  # モジュールから持ってくる
foo: int | None  # コンパイラーに内蔵

def add(x: float, y:float, z:Optional[int]) -> None:
    ...