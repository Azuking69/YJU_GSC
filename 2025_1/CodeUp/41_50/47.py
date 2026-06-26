"""
정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
0 <= a <= 10, 0 <= b <= 10
"""
#1 정수 2개(a, b)를 입력
a, b = input("정수 2개를 입력: ").split()

#2 a를 2b배 곱한 값으로 출력
num_a = int(a)
num_b = int(b)

print(num_a * (2 ** num_b))