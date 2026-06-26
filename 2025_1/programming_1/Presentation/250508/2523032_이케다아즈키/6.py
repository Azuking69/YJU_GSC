# 초기화
result = 0

# 1~20 사이
for i in range(1, 20 + 1):
    # 홀수의 경우 건너뛰기
    if i % 2 == 1:
        continue
    # 짝수의 경우 더하기
    else:
        result += i
# 반복 끝나면 출력
print(f"1부터 20까지의 짝수 합계(홀수 건너뜀): {result}")