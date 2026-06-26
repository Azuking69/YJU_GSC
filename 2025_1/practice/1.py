"""
사용자로부터 2~9 사이의 정수 하나를 입력받아, 해당 단의 구구단 중 
**3의 배수(3, 6, 9)**만 for문으로 출력
"""

#1 숫자를 입력
user_input = int(input("정수를 입력하세요(2~9): "))

#2 저건문(2~9 이외 경우 오류)
if user_input <= 1 or user_input >= 10:
    #오류 출력
    print("오류: 2~9 사이의 정수를 입력하세요")

#3 오류 없을 때 계산
else:
    # 3의 배수만 계산
    for i in range(3, 9 + 1, 3):
        print(f"{user_input} X {i} = {user_input * i}")
