"""
사용자에게 반복적으로 메뉴를 출력
사용자의 선택에 따라 합게, 평균, 지수 계산을 수행하는 프로그램
"""

#1 메뉴 정의
menu = """-----메뉴-------
1. 합계 계산(정수 두 개 입력)
2. 평균 계산(실수 세 개 입력)
3. 지수 계산(밑수 [정수], 지수 [정수] 입력)
4. 종료"""

#2 반복
while True:
    #2-1 메뉴 출력 
    print(menu)
    
    #2-2 사용자 입력
    user_input_menu = int(input("메뉴를 선택하세요: "))
    
    #2-3-1 1.합계 계산(정수 두 개 입력)
    if user_input_menu == 1:
        #2-3-2 사용자 정수를 두 개 입력
        input_number_1 = int(input("첫 번째 정수를 입력하세요: "))
        input_number_2 = int(input("두 번째 정수를 입력하세요: "))
        #2-3-3 계산 결과
        result = input_number_1 + input_number_2
        #2-3-4 출력
        print(f"합계: {result}")
        #2-3-5 행을 바꿈
        print()
    
    #2-4-1 2. 평균 계산(실수 셰 개 입력)
    elif user_input_menu == 2:
        #2-4-2 사용자 실수를 입력
        input_number_1 = float(input("첫 번째 실수를 입력하세요: "))
        input_number_2 = float(input("두 번째 실수를 입력하세요: "))
        input_number_3 = float(input("세 번째 실수를 입력하세요: "))
        #2-4-3 계산 결과
        result = (input_number_1 + input_number_2 + input_number_3) / 3
        #2-4-4 출력
        print(f"평균: {(result)}")
        #2-4-5 행을 바꿈
        print()
        
    #2-5-1 지수 계산(밑수[정수], 지수[정수] 입력)
    elif user_input_menu == 3:
        #2-5-2 사용자 입력
        input_number_1 = int(input("밑수를 입력하세요: "))
        input_number_2 = int(input("지수를 입력하세요: "))
        #2-5-3 계산 결과
        result = input_number_1 ** input_number_2
        #2-5-4 출력
        print(f"결과: {result}")
        #2-5-5 행을 바꿈
        print()
        
    #2-6-1 4. 종료
    elif user_input_menu == 4:
        #2-6-2 출력
        print("프로그램 종료")
        #2-6-3 탈출
        break
    
    #2-7-1 오류문 출력
    else:
        print("잘못된 입력입니다.")
        #2-7-2 행을 바꿈
        print()