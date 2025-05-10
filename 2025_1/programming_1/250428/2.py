# row 반복
for num_row in range(1, row + 1):
        # " " 반복
        for _ in range(row - num_row):
            # " " 출력
            print(" ", end="")

        # "*" 반복
        for _ in range(num_row * 2 - 1):
            # "*" 출력
            print("*", end="")

        print()