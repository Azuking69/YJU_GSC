"""
사용자에게 반복적으로 메뉴를 출력
사용자의 선택에 따라 합계, 평균, 지수 계산을 수행하는 프로그램
"""

#1 메뉴 정의
menu = """
1. 합계 계산 (정수 두 개 입력)
2. 평균 계산 (실수 세 개 입력)
3. 지수 계산 (밑수 [정수], 지수 [정수] 입력)
4. 종료"""

#2 반복문
while True:
    print(menu)
    user_input_menu = int(input("메뉴를 선택하세요: "))
    
    if user_input_menu == 1:
        input_number_1 = int(input("첫 번째 정수를 입력하세요: "))
        input_number_2 = int(input("두 번째 정수를 입력하세요: "))
        result = input_number_1 + input_number_2
        print(f"합계: {result}")
    
    elif user_input_menu == 2:
        input_number_1 = float(input("첫 번째 실수를 입력하세요: "))
        input_number_2 = float(input("두 번째 실수를 입력하세요: "))
        input_number_3 = float(input("세 번째 실수를 입력하세요: "))
        result = (input_number_1 + input_number_2 + input_number_3) / 3
        print(f"평균: {result}")

    elif user_input_menu == 3:
        input_number_1 = int(input("밑수를 입력하세요: "))
        input_number_2 = int(input("지수를 입력하세요: "))
        result = input_number_1 ** input_number_2
        print(f"결과: {result}")

    elif user_input_menu == 4:
        print("프로그램 종료")
        break

    else:
        print("잘못된 입력입니다.")