# 각 메소드의 호출 카운트 확인하고 싶다
class my_util:
    @staticmethod
    def add(a, b):
        return a + b

    def avg(a, b):
        return (a + b) / 2

print(my_util.add(2, 3))
print(my_util.avg(3, 4))