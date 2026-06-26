"""
사용자로부터 2~9 사이의 정수를 입력받아,
해당 단의 구구단 중 곱하는 수가 짝수이고,
결과가 10보다 큰 경우만 출력
"""

#1 정수 입력
while True:
    input_number = int(input("정수를 입력하세요: "))
    #오류 출력
    if input_number <= 1 or input_number >=10:
        print("오류: 2~9의 범위로 입력하세요")
    
    #2 구구단 중 곱하는 수가 짝수
    else:
        for i in range(2, 9 + 1, 2):
            result = input_number * i
            #결과가 10보다 큰 경우
            if result >= 10:
                print(f"{input_number} X {i} = {result}")