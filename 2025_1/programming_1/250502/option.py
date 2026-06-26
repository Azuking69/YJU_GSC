"""
옵션 5
***
***
***
1. 테두리(枠)
2. 왼쪽
3. 오른쪽
4. 양방향 대각선(双方向の対角線)
"""

# 옵션 선택
user_select_menu = int(input("""출력 옵션을 선택하세요: 
1. 테두리
2. 왼쪽
3. 오른쪽
4. 양방향 대각선
옵션 (1 ~ 4): """))

# 범위 설정
for row in range(3):
    for col in range(3):
        # 1. 테두리
        if user_select_menu == 1:
            # 별 만들기
            if row == 0 or row == 2 or col == 0 or col == 2:
                print("*", end="")
            # 빈칸 만들기
            else:
                print(" ", end="")

        # 2. 왼쪽
        elif user_select_menu == 2:
            # 별 만들기
            if col == 0:
                print("*", end="")
            # 빈칸 만들기
            else:
                print(" ", end="")
            
        # 3. 오른쪽
        elif user_select_menu == 3:
            # 별 만들기
            if col == 2:
                print("*", end="")
            # 빈칸 만들기
            else:
                print(" ", end="")
            
        # 4. 양방향 대각선
        else:
            if row == col or row + col == 2:
                # 별 만들기
                print("*", end="")
            # 빈칸 만들기
            else:
                print(" ", end="")
    print()