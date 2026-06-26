"""
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
n번째 수를 출력하는 프로그램을 만들어보자.
"""
#1 시작 값, 곱할 값, 더할 값, 몇 번째 인지를 나타내는 정수가 공백을 두고 입력
a, m, d, n = input("공백을 두고 입력: ").split()

#2 int형으로 변환
a = int(a)
m = int(m)
d = int(d)
n = int(n)

#3 n번째 수를 출력
result = a
for _ in range(n - 1):
    result = result * m + d

#4 출력
print(result)