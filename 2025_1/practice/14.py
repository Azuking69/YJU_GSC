"""
사용자로부터 테이블 개수 T, 각 테이블의 행 수 M, 열 수 N을 입력 받아
다음과 같이 숫자로 채워진 M×N 테이블을 T개 출력하는 프로그램을 작성
"""
#1 사용자로부터 테이블 개수 T, 각 테이블의 행 수 M, 열 수 N을 입력 받는다
input_T = int(input("테이블 개수를 입력하세요: "))
input_M = int(input("각 테이블의 행 수를 입력하세요: "))
input_N = int(input("열 수를 입력하세요: "))

#2 테이블 작성
num = 1
for _ in range(input_T):
    #3 각 테이블의 행 작성
    for _ in range(input_M):
        #4 열 작성
        for _ in range(input_N):
            #5 출력
            print(f"{num:2}", end=" ")
            num += 1
        #6 행 바꾸기
        print()
    #7 행 바꾸기
    print()