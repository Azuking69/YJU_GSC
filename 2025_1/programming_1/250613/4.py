bar = {"std1" : 10, "std2" : 20, "std3" : 30}

#print(bar.keys())
keys = bar.keys()

if "std1" in keys:
    print("True")
else:
    print("Fales")

# Create
if "std4" not in keys:
    bar["std4"] = 100