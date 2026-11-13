class Bar:
    def __init__(self) -> None:
        self.__data = [10, 20, 30]
        self.__count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__count += 1

        if self.__count < len(self.__data):
            return self.__data[self.__count]

        raise StopIteration
    
obj = Bar()
it = iter(obj)
    
print(next(it))   # 10
print(next(it))   # 20
print(next(it))   # 30
print(next(it))   # StopIteration