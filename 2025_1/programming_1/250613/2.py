#bar = []
#bar[0] = 10
#print(bar)

bar = {}
bar[0] = 10
bar["0"] = 20
bar[0.0] = 30
bar[True] = 40
bar[(1, 2)] = 50
print(bar)