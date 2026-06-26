bar = [val for val in range(1, 11, 2)]
# bar = [1, 3, 5, 7, 9]
# [], list()

foo = list(bar)
pos = bar.copy()
kin = bar[:]

bar[0] = 100
print(foo)
print(pos)
print(kin)