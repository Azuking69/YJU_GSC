#1 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력
#  두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력
import random
n = int(input("첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력: "))
a = [random.randint(1, 23) for _ in range(n)]
print(a)
#2 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력
d = []
for _ in range(23 + 1):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

#3 출력
for i in range(1, 24):
    print(d[i], end=" ")