"""
주사위(さいころ) 던지기 결과의 빈도를 분석하고, 히스토그램을 통해
결과를 시각화하는 프로그램을 작성
"""
import random

while True:
    #1. 사용자 입력
    # 사용자로부터 주사위를 던질 횟수 N을 입력받는다
    input_N = int(input("Enter the number of dice rolls(between 100 and 1,000,000): "))
    # 유효하지 않은 값을 입력할 경우, 재입력을 요청한다
    if input_N < 100 or 1000000 < input_N:
        print("Please enter a number within the specified range.")

    #2. 난수 생성 및 카운트
    else:
        # 사용자가 입력한 횟수 N만큼 주사위를 던진다
        num_list = [random.randint(1, 6) for _ in range(input_N + 1)]
        # 각 숫자의 발생 횟수를 카운트한다
        count_list = [0] * 6

        # 숫자 발생 횟수를 카운트
        for num in num_list:
            count_list[num - 1] += 1
        
        # 최대값 구하기
        max_count = count_list[0]
        for _ in count_list:
            if num > max_count:
                max_count = num

        #3. 결과 시각화
        print("\nDice Roll Frequency Histgram:")
        # 1부터 6까지 각 숫자의 발생 빈도를 히스토그램으로 시각화한다
        for i in range(6):        
            # 히스토그램에서 각 *는 발생 빈도의 최대치에 대한 상대적인 비율로 나타나며, 
            # 최대 10개의 *를 표시한다
            ind_count = count_list[i]
            dice_per = (ind_count / input_N) * 100
            star_count = "*" * int((ind_count / max_count) * 10)
            # 각 숫자별로 발생 횟수와 확률을 표시한다
            print(f"{i + 1}: {star_count}({ind_count} times, {dice_per:.2f}%)")