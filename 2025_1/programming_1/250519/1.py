bar = [val for val in range(1, 11, 2)]
# bar = [1, 3, 5, 7, 9]

pos = foo = bar
# pos = bar
# pos = bar

pos[0] = 10
foo[-1] = 100
print(foo)