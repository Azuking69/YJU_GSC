"""
출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.
"""
import random
#1 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력
n = int(input("번호를 부른 횟수: "))

#2 n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력
a = [random.randint(1, 23) for _ in range(n)]
print(a)

#3 출석을 부른 번호 순서를 바꿈 
for i in range(n-1, -1, -1):
    
    #4 공백을 두고 출력
    print(a[i], end=" ")