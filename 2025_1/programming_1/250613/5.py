bar = {"std1" : 10, "std2" : 20, "std3" : 30}

# Create
if bar.setdefault("std4", 200) == 200:
    print("입력 성공!")
else:
    print("입력 실패")

print(bar.setdefault("std1", 100))
print(bar)