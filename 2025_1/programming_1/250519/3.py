bar = [val for val in range(1, 11, 2)]
# bar = [1, 3, 5, 7, 9]

for val in range(2, 11, 2):
    print(val, end="\t")
# bar = [2, 4, 6, 8, 10]

print(bar[2 : 11 : 2])
print(bar[0 : 5 : 1])
print(bar[0 :])
print(bar[2 :])
print(bar[2 : 4])
print(bar[2 : 3])
print(bar[2 : -1])