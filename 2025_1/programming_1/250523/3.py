bar = [1, 20, 5, 100, 200]

print(100 in bar)
print(100 not in bar)

for val in bar:
    if val == 100:
        print("100")
        break