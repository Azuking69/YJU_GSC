
bar: int = 2

bar = 3.0
bar = "3"
bar = True

def add(a: int, b: int| str) -> :
    return a + int(b)


add(2, 2)
add(2, "2")
add("3", 2)

result1: str = add(2, 2)
result2: int = add(2, 2)