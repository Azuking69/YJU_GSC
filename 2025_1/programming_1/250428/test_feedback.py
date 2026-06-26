# 반복
while True:
    # 메뉴 출력
    print("""-----메뉴-----
          1. 합계
          2. 평균
          3.지수
          4. 종료""")

    # 메뉴 입력
    input_num = int(input("메뉴를 선택 하세요"))

    # 입력된 메뉴에 따라 프로그램 실행
    # 1번 합계
    if input_num == 1:
        input_num_1 = int(input("첫 번째 값을 입력하세요: "))
        input_num_2 = int(input("두 번째 값을 입력하세요: "))
        print(f"합계: {input_num_1 + input_num_2}")
    # 2번 평균
    elif input_num == 2:
        input_num_1 = int(input("첫 번째 값을 입력하세요: "))
        input_num_2 = int(input("두 번째 값을 입력하세요: "))
        input_num_3 = int(input("세 번째 값을 입력하세요: "))
        print(f"평균: {(input_num_1 + input_num_2 + input_num_3) / 3}")
    # 3번 지수
    elif input_num == 3:
        input_num_1 = int(input("첫 번째 값을 입력하세요: "))
        input_num_2 = int(input("두 번째 값을 입력하세요: "))
        print(f"결과: {input_num_1 ** input_num_3}")
    # 4번 종료