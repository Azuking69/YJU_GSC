# [1, 2, 3, 4, 5]
bar = [val for val in range(1, 6)]

# * -> collection -> list
a, *b, c = bar
print(a, b, c)