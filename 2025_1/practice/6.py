"""
2~9 사이의 두 정수 A, B를 입력받아, 
A단부터 B단까지 5의 배수만 for문으로 출력
"""

#1 정수 입력
input_number_1 = int(input("첫 번째 숫자를 입력(2~9): "))
input_number_2 = int(input("두 번째 숫자를 입력:(2~9) "))
# 오류 출력
if input_number_1 <= 1 or input_number_1 >= 10 or input_number_1 > input_number_2 :
    print("오류: 첫 번째 숫자는 2~9사이의 정수를 입력하세요.")
    print("두 번째 숫자는 첫 번째 숫자보다 크게 입력하세요.")

#2 
else:
    for i in range(input_number_1, input_number_2 + 1):
        print("==========")
        for j in range(1, 9 + 1):
            print(f"{i} X {j} = {i * j}")