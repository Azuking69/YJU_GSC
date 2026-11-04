class Vector:
    def init(self, x:int, y:int) -> None:
    self.__x: int = x
    self.__y: int = y

def __str__(self) -> str:
    return f"Vector: x {self.__x}, y {self.__y}"

def __add__(self, other:Vector)->Vector:
    x = self.__x + other.__x
    y = self.__y + other.__y
    return Vector(x, y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)