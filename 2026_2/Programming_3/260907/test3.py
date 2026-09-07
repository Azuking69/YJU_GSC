class Util:
    @classmethod
    def add(cls, *arg_list):
        return sum(arg_list)

    @classmethod
    def avg(cls, *arg_list):
        return sum(arg_list) / len(arg_list)

print(Util.add(1, 2, 3))
print(Util.avg(1, 2, 3))