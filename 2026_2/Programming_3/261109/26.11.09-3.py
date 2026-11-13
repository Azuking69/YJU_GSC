class Bar:
    def __init__(self) -> None:
        self.__data = [10, 20, 30]
        self.__y = [100, 200, 300]
        self.__count = -1

    def __iter__(self):
        return self

    def __getitem__(self, key:int):
        return self.__data[key], self.__y[key]
    
    def __next__(self):
        self.__count += 1

        if self.__count < len(self.__data):
            return self.__data[self.__count], self.__y[self.__count]

        raise StopIteration

    def __len__(self):
        return len(self.__data)

    def __eq__(self, value:Bar) -> bool:
        return self.__data == value.__data and self.__y == value.__y

    def __contains__(self, item:tuple):
        return item[0] in self.__data and item[1] in self.__y

    def __setitem__(self, key, value):
        self.__data[key] = value[0]
        self.__y[key] = value[1]

    def __str__(self) -> str:
        msg = ""
        for x, y in zip(self.__data, self.__y):
            msg += f"x: {x}, y: {y}"

        return msg

obj = Bar()
obj[2] = (40, 400)
print(obj)

# obj = Bar()
# print((30, 300) in obj)

# a = [1, 2, 3]

# print(3 in a)   # True
# print(4 in a)   # False
# print(a.__contains__(4))  # False

# obj_a = Bar()
# obj_b = Bar()

# print(obj_a == obj_b)   # True

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)   # True
# print(a.__eq__(b))   # True

# print(len(obj))

# x, y = obj[1]
# print(x, y)

# for x,y in obj:
#     print(x,y) 