"""
range(시작값,  종료값, 증감값)
range(시작값,  종료값)
range(증감값)
"hello"
10, 9, 8,...0
"""

for num in range(5):
    print(f"{num}")

for num in range(10, -1, -1):
    print(f"{num}")

for _ in range(5):
    print(f"{num}")

for num in "abc":
    print(f"{num}, end = "" ")

for t in range(3):
    for i in range(4):
        for j in range(3):
            for p in range(2):
                print(f"{p}")