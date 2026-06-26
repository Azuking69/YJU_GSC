"""
사용자로부터 하나의 정수를 입력받아 해당 수의 구구단을 for문을 이용하여 출력
단, 출력은 짝수 곱셈 결과만 출력되도록 하며, 출력 형식은 3번 참조
"""
#1 정수 입력
# 범위는 2~9
input_number = int(input("출력할 단을 입력하세요(2~9): "))

#2 입력된 정수를 검사
# 1이하 10이상인 경우 오류 출력
if input_number <= 1 or input_number >= 10:
    #출력
    print("오류: 2단부터 9단까지만 입력 가능합니다")
    
else:
    #3 구구단 작성
    # 짝수의 경우
    for i in range(2, 8 + 1, 2):
        #출력
        print(f"{input_number} X {i} = {input_number * i}")