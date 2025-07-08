"""
3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
"""
#1 3개의 정수 입력
a, b, c = input("3개의 정수 입력: ").split()

#2 변환
num_a = int(a)
num_b = int(b)
num_c = int(c)

#3 짝수만 출력
if num_a % 2 == 0:
    print(num_a)

if num_b % 2 == 0:
    print(num_b)

if num_c % 2 == 0:
    print(num_c)