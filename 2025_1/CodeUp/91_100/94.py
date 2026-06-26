"""
출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
"""
import random
#1 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력
n = int(input("번호를 부른 횟수 입력: "))

#2 n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력
k = [random.randint(1, 10) for _ in range(n)]
print(k)

#3 출석을 부른 번호 중에 가장 빠른 번호를 출력
num = min(k)
print(num)