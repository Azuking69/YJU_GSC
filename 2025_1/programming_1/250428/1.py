"""
*****
*****
*****
"""

row = 5
col = 9

# row 반복
for num_row in range(1, row + 1):
    # col 반복
    for _ in range(num_row):
        # "*" 출력
        print("*", end="")
    
    print()

for num_row in range(row - 1, 0, -1):
    for _ in range(num_row):
        print("*", end="")

    print()

