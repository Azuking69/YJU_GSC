"""
주사위(さいころ) 던지기 결과의 빈도를 분석하고, 히스토그램을 통해
결과를 시각화하는 프로그램을 작성
"""
import random

while True:
    #1 사용자 입력
    #1-1 입력 범위는 100에서 1,000,000 사이
    dice_count = int(input("Enter the number of dice rolls (between 100 and 1,000,000): "))

    #1-2 유효하지 않은 값을 입력할 경우, 재입력을 요청
    if dice_count < 100 or 1000000 < dice_count:
        print("Please enter a number within the specified range.")

    #2 난수 생성 및 카운트
    else:
        #2-1 사용자가 입력한 횟수 N만큼 주사위를 던진다
        #2-2 주사위의 결과는 1부터 6 사이의 숫자
        num_list = [random.randint(1, 6) for _ in range(dice_count + 1)]
        counts = [0] * 6
      
        #2-3 각 숫자의 발생 횟수를 카운트
        for num in num_list:
            counts[num - 1] += 1

        max_count = max(counts)

        #3 결과 시각화
        #3-1 1부터 6까지 각 숫자의 발생 빈도를 히스토그램으로 시각화
        print("\nDice Roll Frequency Histogram:")
        for i in range(6):
            #3-2 히스토그램에서 각 *는 발생 빈도의 최대치에 대한 상대적인 비율로 나타나며, 
            #    최대 10개의 *를 표시
            individual_count = counts[i]
            per = (individual_count / dice_count) * 100
            stars = "*" * round((individual_count / max_count) * 10)

            #4 각 숫자별로 발생 횟수와 확률을 표시한다
            print(f"{i + 1}: {stars}({individual_count}times, {per:.2f}%)")
            break