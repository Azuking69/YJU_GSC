# iteration : 순회
bar = [10, 20, 30, 40, 50]

print(bar[0], bar[1], bar[2], bar[3], bar[4])

for idx in range(len(bar)):
    print(bar[idx])

for val in bar:
    print(val)

for val in bar:
    print(f"{idx} index: {val}")
    idx += 1

for idx, val in enumerate(bar):
    print(f"{idx} index: {val}")

[Unpacking]
pos, kin, sol = [2, 3, 4]
print(pos, kin, sol)

# 0 index : 10
# 1 index : 20
