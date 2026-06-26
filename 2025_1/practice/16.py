"""
사용자로부터 정수 리스트 개수를 입력받고, 무작위로 숫자를 생성하여 최대값, 
최소값, 중앙값, 평균, 표준편차를 출력하는 프로그램을 작성
"""
import random
import math

#1 사용자로부터 정수 리스트 개수를 입력받는다
#  (리스트 개수는 반드시 5 이상 30 이하의 정수)
input_num = int(input("리스트 개수를 입력하세요(5~30): "))

#2 범위 외의 경우
if input_num < 5 or 30 < input_num:
    print("잘못된 입력입니다.")


else:
    #3 리스트 작성
    num_list = []
    for _ in range(input_num):
        num = random.randint(1, 100)
        num_list.append(num)
    print(f"생성된 리스트: {num_list}")

    #4 최대값 출력
    max_val = num_list[0]
    for i in range(1, len(num_list)):
        if max_val < num_list[i]:
            max_val = num_list[i]
    print(f"최대값: {max_val}")

    #5 최소값 출력\
    min_val = num_list[0]
    for i in range(1, len(num_list)):
        if min_val > num_list[i]:
            min_val = num_list[i]
    print(f"최소값: {min(num_list)}")

    #6 중앙값 출력
    sorted_list = num_list[:]
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    n = len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    
    print(f"중앙값: {median}")

    #7 평균 출력
    sum_num = 0
    for i in range(len(num_list)):        
        sum_num += num_list[i]
    avg_num = sum_num / len(num_list)
    print(f"평균: {avg_num}")

    #8 편차
    n_a_list = []
    for i in range(len(num_list)):
        n_a_num = round(num_list[i] - avg_num, 2)
        n_a_list.append(n_a_num)
    print(f"편차: {n_a_list}")

    #9 분산 출력
    breakup_sum = 0
    for i in range(len(n_a_list)):
        breakup_sum += n_a_list[i] ** 2
        breakup_avg = round(breakup_sum / len(n_a_list), 2)
    print(f"분산: {breakup_avg}")

    #10 표준편차 출력
    std_dev = math.sqrt(breakup_avg)
    print(f"표준편차: {round(std_dev, 2)}")