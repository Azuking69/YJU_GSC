sum = 0

for i in range(1, 21):
    if i % 2 == 0:
        sum += i
    else:
        continue

print(f"1부터 20까지의 짝수 합계(홀수 건너뜀): {sum}")