bar = [1, 2, 3]
foo = (4, 5, 6)

print(bar, type(bar), bar[1])
print(foo, type(foo), foo[1])

# list
bar[0] = 100
bar.append(100)
# tuple
foo[0] = 200
foo.append(200)