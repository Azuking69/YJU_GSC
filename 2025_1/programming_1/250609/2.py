def foo(a, b, c=100, d=200, e=300):
    print(a, b, c)


foo(1, 2, 3)
foo(a=1, c=3, b=2)
foo(3, 2, d=1000)