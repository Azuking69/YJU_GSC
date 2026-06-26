"""
프로그램은 더하기, 빼기, 곱하기, 나누기 중 하나의 연산을 수행
"""
import sys

#숫자 입력
baseValue = float(input("기본값을 입력하세요: "))

#선택
menu = """===========
1. 더하기
2. 빼기
3. 곱기
4. 나누기기
===========
"""
print(menu)
user_colect = int(input("선택: "))

#계산할 때 사용할 숫자 입력
user_number = float(input("숫자 입력: "))

#정의
def selectOperation():
    if user_colect == 1:
        result_number = baseValue + user_number
        return result_number
    elif user_colect == 2:
        result_number = baseValue - user_number
        return result_number
    elif user_colect == 3:
        result_number = baseValue * user_number
        return result_number
    elif user_colect == 4:
        if user_number <= 0:
            print("에러: 0으로 나눌 수 없습니다.")
            sys.exit()
        else:
            result_number = baseValue / user_number
            return result_number

#출력
print(f"연산 결과: {selectOperation()}")       