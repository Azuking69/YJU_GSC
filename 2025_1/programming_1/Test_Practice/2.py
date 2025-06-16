"""
주사위(さいころ) 던지기 결과의 빈도를 분석하고, 히스토그램을 통해
결과를 시각화하는 프로그램을 작성
"""
import random

while True
    # 입력 (범위: 100 ~ 1,000,000)
    dice_count = int(input("Enter the number of dice rolls(between 100 and 1,000,000): "))

    # 범위외 오류
    if dice_count < 100 or 1000000 < dice_count:
        print("Please enter a number within the specified range.")

    else:
        # 주사위(1~6) 던지기
        dice_list = [random.randint(1, 6) for _ in range(dice_count)]
        # 각 숫자마다 list생성
        count = [0] * 6
        
        # 나온 값을 
        for num in dice_list:
            count[num - 1] += 1