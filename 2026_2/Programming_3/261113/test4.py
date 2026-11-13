class MyData:
    def __init__(self):
        self._data = [10, 20, 30]

    def __iter__(self):
        print("시작")
        yield from self._data
        print("종료")

obj = MyData()
for value in obj:
    print(value)