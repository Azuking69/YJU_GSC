class MyDataset:   # 데이터를 저장하는 Iterable 객체
    def __init__(self, x:list, y:list) -> None:
        self.__features = x
        self.__label = y

    # Iterator를 반환하는 매서드
    def __iter__(self):    # 새로운 Iterator를 생성해서 반환
        return MyDatasetIteration(self.__features, self.__label)

class MyDatasetIteration:   # 데이터를 하나씩 반환하는 Iterator 객체
    def __init__(self, x:list, y:list) -> None:
        self.__features = x
        self.__label = y
        self.__count = -1

    def __next__(self):     # 다음 데이터 반환
        self.__count += 1
        if self.__count < len(self.__features):
            return self.__features[self.__count], \
                self.__label[self.__count]
            
        raise StopIteration   # 더 이상 반환할 데이터가 없음을 알림

dataset = MyDataset([1, 2], [3, 4])

for x, y in dataset:   # -> __iter__
    for x, y in dataset:   # -> __iter
        print(f"x: {x}, y: {y}")

pos = [1, 2, 3]
print(type(iter(pos)))   # iter(pos) -> 리스트의 Iterator 생성