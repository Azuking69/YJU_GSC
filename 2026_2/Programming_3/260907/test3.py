class Util:
    @classmethod
    def add(cls, *arg_list):
        return sum(arg_list)

print(Util.add(1, 2, 3))