for num_row in range(1, row + 1):
        # " " 반복
        if num_row % 2 ==0:
             # " " 출력
             print()
             continue

        # "*" 반복
        for _ in range(num_row * 2 - 1):
            # "*" 출력
            print("*", end="")

        print()