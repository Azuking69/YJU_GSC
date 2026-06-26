bar = {"a" : 10, "b" : 20, "c" : 30}

def prt(**kwargs):
    for key in kwargs.keys():
        print(f"Key: {key}")

prt(**bar)