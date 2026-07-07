def test(arg):
    print(f"arg: {arg}")

bar = [test(value) for value in range(1, 6)]

print(bar)