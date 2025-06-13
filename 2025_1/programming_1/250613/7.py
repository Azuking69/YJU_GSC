bar = {"std1" : 10, "std2" : 20, "std3" : 30}

# Read
print(bar.get("std4"))
print(bar.get("std1"))
print(bar.get("std5", False))