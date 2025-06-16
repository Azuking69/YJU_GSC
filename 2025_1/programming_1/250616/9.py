bar = ["a", "b", "c"]
foo = [10, 20, 30]
pos = [100, 200, 300]

result = dict(zip(bar, foo))

for key, value in result.items():
    print(key, value)