from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sounds(self):
        pass

class Dog(Animal):
    def sounds(self):
        print("멍멍")

class Cat(Animal):
    def sounds(self):
        print("야옹")

class Tiger(Animal):
    def sounds(self):
        print("어흥")

def make_sound(obj):
    obj.sounds()


obj_1 = Dog()
obj_2 = Cat()

make_sound(obj_1)
make_sound(obj_2)
make_sound(Tiger())