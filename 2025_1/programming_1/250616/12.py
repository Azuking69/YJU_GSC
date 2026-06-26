def bar(a, *b, c = 10, **kwargs):
    print(a)
    print(b)
    print(c)
    print(kwargs)

foo = [val for val in range(1, 10)]
pos = {'d' : 10, 'e' : 20, 'f' : 30}
bar(*foo, **pos)