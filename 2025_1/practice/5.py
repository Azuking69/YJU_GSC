"""
사용자로부터 2~9 사이의 정수 하나를 입력받아
1~9 중 그 단으로 나누어떨어지지 않는 수만 구구단 결과로 출력
"""

#1 정수 입력
input_number = int(input("정수를 입력하세요(2~9): "))
#오류 출력
if input_number <= 1 or input_number >= 10:
    print("오류: 2~9사이의 정수를 입력하세요.")

else:
    # 구구단
    for i in range(1, 9 + 1):
        # 결과
        result = input_number * i
        # 입력 숫자로 나눌 수 있을 때 출력
        if result % 2 == 1:
            print(f"{input_number} X {i} = {result}")