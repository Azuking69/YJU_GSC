def bar(a, b, *c):
    print(a, b)
    print(c)

foo = [val for val in range(1, 10)]
bar(*foo)