"""
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
"""
#1 정수(1 ~ 100) 1개를 입력
num = int(input("정수(1 ~ 100) 1개를 입력: "))

#2 1부터 그 수까지 짝수의 합을 구한다
result = 0
for i in range(num + 1):
    if i % 2 == 1:
        continue
    else:
        result += i

# 출력
print(result)