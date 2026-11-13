def test():
    yield 1
    yield from [10, 20, 30]
    yield [10, 20, 30]
    yield "abc"
    yield from "def"

for value in test():
    print(value)
