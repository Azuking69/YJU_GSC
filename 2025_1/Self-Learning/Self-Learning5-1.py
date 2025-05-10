"""
세 개의 정수를 입력 받는다
세 수의 관계에 따라 다음과 같이 출력
"""

#1 입력
input_number1 = int(input("첫 번째 수 입력: "))
input_number2 = int(input("두 번째 수 입력: "))
input_number3 = int(input("세 번째 수 입력: "))

#2 결과 정의
if input_number1 == input_number2 == input_number3:
    print("모든 수가 같습니다.")
elif input_number1 == input_number2 or input_number1 == input_number3 or input_number2 == input_number3:
    if input_number1 == input_number2:
        print(f"두 수가 같습니다.({input_number1}와 {input_number2})")
    elif input_number1 == input_number3:
        print(f"두 수가 같습니다.({input_number1}와 {input_number3})")
    else:
        print(f"두 수가 같습니다.({input_number2}와 {input_number3})")
else:
    max_number = input_number1
    if max_number > input_number2:
        max_number = input_number2
    else:
        max_number = input_number3
    
    print(f"모든 수가 다릅니다. 가장 큰 수는 3입니다.")
