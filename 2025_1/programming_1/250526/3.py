# [1, 2, 3, 4, 5]
bar = [val for val in range(1, 6)]

foo = [1, 2, 3]
pos = [4, 5, 6]

for x, y in zip(foo, pos):
    print(f"{x}, {y}")