class Util:
    cnt_add = 0; cnt_avg = 0
    @classmethod
    def add(cls, *arg_list):
        cls.cnt_add += 1
        return sum(arg_list)

    @classmethod
    def avg(cls, *arg_list):
        cls.cnt_avg += 1
        return sum(arg_list) / len(arg_list)

print(Util.add(1, 2, 3))
print(Util.avg(1, 2, 3))