class Bar:
    def __init__(self, name:str, age:int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"name: {self._name}, age: {self._age}"

    def __eq__(self, oprnd: "Bar") -> bool:
        return self._name == oprnd._name and\
                self._age == oprnd._age

    def __lt__(self, other: "Bar") -> bool:
        return self._age < other._age

    def __le__(self, other: "Bar") -> bool:
        return self._age <= other._age 
    

obj1 = Bar("gsc", 20)
# obj2 = Bar("gsc", 20)
obj2 = Bar("yju", 30)

# print(obj1 == obj2)
# print(obj1 < obj2)
print(obj1 <= obj2)