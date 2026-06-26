#bar = []
#bar[0] = 10
#print(bar)

bar = {}
bar[0] = 10
bar["0"] = 20
bar[0.0] = 30
bar[True] = 40

class Foo:
    pass

obj = Foo()

bar[obj] = 200

print(bar)