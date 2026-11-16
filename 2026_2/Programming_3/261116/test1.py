# 제네레이터 -> 이터레이터를 구현할 필요가 없다

class Bar:
    def __init__(self):
        self._data = [10, 20, 30]

    def __iter__(self):
        yield from self._data

obj = Bar()

for value_1 in obj:
    for value_2 in obj:
        print(value_1, value_2) # 0 0 0 1 0 2 0 3 0 4 1 1 1 2 1 3 1 4 2 2 2 3 2 4 3 3 3 4 4
