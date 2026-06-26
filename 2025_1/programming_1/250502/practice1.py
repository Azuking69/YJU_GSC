"""
사용자로부터 테이블 개수 T, 각 테이블의 행 수 M, 열 수 N을 입력 받아
*로 구성된 MxN 테이블을 T개 출력
"""
# 입력
# 정수 T (테이블 개수)
input_table = int(input("테이블 개수 입력: "))
# 정수 M (행 수)
input_row = int(input("행 수 입력: "))
# 정수 N (열 수)
input_col = int(input("열 수 입력: "))

# 출력 : 입력된 크기만큼의 테이블을 *로 출력
# 테이블
for _ in range(input_table):
    #행 수
    for _ in range(input_row):
        # 열 수
        print("*" * input_col)
# 테이블마다 행을 바꿈
    print()