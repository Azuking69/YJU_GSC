"""
높이가 5인 다이아몬드 형태의 별을 출력
"""
# 높이 정의
height = 5

# 상단
# for문으로 빈칸을 만들기
# 1 <= height <= 5
for height_num in range(1, height + 1):
    # 왼쪽에 빈칸 만들기　range(height = 5 - height_num)
    for _ in range(height - height_num):
        # 출력
        print(" ", end="")
    
    # 별 만들기
    for _ in range(height_num * 2 - 1):
        # 출력
        print("*", end="")
    # 모두 출력
    print()

# 하단
# 1 <= height <= 5(줄다다)
for height_num in range(height, 0, - 1):
    # 빈칸 만들기
    for _ in range(height - height_num):
        # 출력
        print(" ", end="")

    # 별 만들기
    for _ in range(height_num * 2 - 1):
        # 출력
        print("*", end="")
    
    # 모두 출력
    print()