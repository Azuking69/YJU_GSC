# foo.py

print(__name__) #foo

def add(x:int, y:int) -> str:
    return f"Sum: {(x + y)}"

if __name__ == "__main__":
    print(add(3, 2))