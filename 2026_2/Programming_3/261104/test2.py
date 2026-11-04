# Magic Method
# __메소드 이름__

bar = 2
print(bar + 2)
print(bar)

class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector: x={self.x}, y={self.y}"

    def __add__(self, other:Vector) -> Vector:
        x = self.__x + other.__x
        y = self.__y + other.__y
        return Vector(x, y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2  # TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
print(v3)  # Vector: x=4, y=6