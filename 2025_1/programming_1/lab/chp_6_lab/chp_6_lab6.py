"""
 1부터 20까지의 정수 중 짝수의 합계 계산
"""
num_sum = 0

#1 1부터 20까지의 정수 정의
for num in range(1, 20 + 1):
    #2 홀수를 건너뛰고 짝수의 합계를 계산
    if num % 2 == 1:
        continue
    else:
        num_sum += num

#3 출력
print(f"1부터 20까지의 짝수 합계 (홀수 건너뜀): {num_sum}")