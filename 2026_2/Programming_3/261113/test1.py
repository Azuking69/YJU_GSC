class MyData:
    def __init__(self) -> None:
        self._data = [10, 20, 30]
        self._cnt = -1

    # Iteration
    def __iter__(self):
        return MyDtaIterator(self._data)


class MyDtaIterator:
    def __init__(self, data) -> None:
        self._data = data
        self._cnt = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._cnt += 1

        if self._cnt < len(self._data):
            return self._data[self._cnt]

        return StopIteration


data = MyData()


for value in data:
    print(value)