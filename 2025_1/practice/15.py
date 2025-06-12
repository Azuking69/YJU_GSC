"""
사용자로부터 테이블 개수 T, 행 수 M, 열 수 N을 입력받고,
출력 옵션을 선택하여 아래 방식 중 하나로 테이블을 출력
"""

#1 입력
input_T = int(input("테이블 개수를 입력하세요: "))
input_M = int(input("행 수를 입력하세요: "))
input_N = int(input("열 수를 입력하세요: "))
input_menu = int(input("""출력 옵션를 입력하세요.(1, 2 또는 3 중 선택)
1: 순차 숫자 증가 (→ 열 방향 순서대로 숫자 증가)
2: 랜덤 숫자 채우기 (1~100 사이의 정수)
3: 지그재그 순차 증가 → 짝수 행은 왼쪽 → 오른쪽, 홀수 행은 오른쪽 → 왼쪽
: """))

#2 옵션 정의
#2-1 순차 숫자 증가 (→ 열 방향 순서대로 숫자 증가)
if input_menu == 1:
    #2-1-1 출력 시작 값
    count = 1
    #2-1-2 메트릭스 작성
    #2-1-3 데이블 작성
    for table in range(input_T):
        print(f"테이블 {table + 1}")
        #2-1-4 행 작성
        for _ in range(input_M):
            #2-1-5 열 작성
            for _ in range(input_N):
                    print(f"{count:2}", end=" ")
                    #2-1-6 다음 값
                    count += 1
            #2-1-7 행 바꾸기
            print()
        #2-1-8 행 바꾸기
        print()
        #2-1-9 행 바꾸기
    print()

#2-2 랜덤 숫자 채우기（1~100）
elif input_menu == 2:
    import random
    #2-2-1 데이블 작성
    for table in range(input_T):
        print(f"테이블 {table + 1}")
        #2-2-2 행 작성
        for _ in range(input_M):
            #2-2-3 열 작성
            for _ in range(input_N):
                    count = random.randint(1, 100)
                    print(f"{count:2}", end=" ")
            #2-1-7 행 바꾸기
            print()
        #2-1-8 행 바꾸기
        print()
        #2-1-9 행 바꾸기
    print()

#2-3 지그재그 순차 증가 → 짝수 행은 왼쪽 → 오른쪽, 홀수 행은 오른쪽 → 왼쪽
else:
    count = 1
    for table in range(input_T):
        print(f"테이블 {table + 1}")
        for row in range(input_M):
            line = []
            for _ in range(input_N):
                line.append(count)
                count += 1
            if row % 2 == 1:
                line.reverse()
            for num in line:
                print(f"{num:2}", end=" ")
            print()
        print()