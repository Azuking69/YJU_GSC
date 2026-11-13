class MyData:
    def __init__(self) -> None:
        self._data = [10, 20, 30]

    # Iteration
    def __iter__(self):
        yield from self._data


data = MyData()

for value in data:
    for s_value in data:
        print(value, s_value)