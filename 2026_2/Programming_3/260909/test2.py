# add  메소드의 호출 카운트 확인하고 싶다
class my_util:
    add_clk_cnt = 0

    @classmethod
    def add(cls, a, b):
        cls.add_clk_cnt += 1
        return a + b

    @staticmethod
    def avg(a, b):
        return (a + b) / 2

print(my_util.add(2, 3))
print(my_util.avg(3, 4))