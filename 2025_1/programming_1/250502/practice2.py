"""
1단계와 동일하게 T, M, N을 입력받고, 출력 옵션을 선택하여 출력
"""
# random 모듈
import random

# 입력
# 정수 T (테이블 개수)
input_table = int(input("테이블 개수 입력: "))
# 정수 M (행 수)
input_row = int(input("행 수 입력: "))
# 정수 N (열 수)
input_col = int(input("열 수 입력: "))

# 옵션 선택
user_select_menu = int(input("""출력 옵션을 선택하세요: 
1. 1부터 시작하여 열 방향으로 증가
2. 1~100 사이 랜덤 값 출력
옵션 (1 또는 2): """))

# random 숫자 정의
random_num = random.randint(1, 100)

#1 순차 숫자 출력: 1부터 시작하여 열 방향으로 증가
if user_select_menu == 1:
    # 테이블 범위
    for i in range(1, input_table + 1):
        num = 1 # 수자 정의(테이블마다 reset)
        print() # 행을 바꿈
        print(f"테이블{i}", end="") # 테이블명 출력
        # 행 개수
        for _ in range(input_row):
            print() # 입력된 수자로 나누기
            # 열 개수
            for _ in range(input_col):
                print(num, end="     ") # 출력
                num += 1 # 1씩 더하기
        # # 테이블마다 나누기
        print()

# 1이외
else:
    # 테이블 범위
    for i in range(1, input_table + 1):
        print() # 행을 바꿈
        print(f"테이블{i}", end="") # 테이블명 출력
        # 행 개수
        for _ in range(input_row):
            print() # 입력된 수자로 나누기
            # 열 개수
            for _ in range(input_col):
                print(random_num, end=" ") # 출력
                random_num += 1 # 1씩 더하기 
       
        # 테이블마다 나누기        
        print()
        