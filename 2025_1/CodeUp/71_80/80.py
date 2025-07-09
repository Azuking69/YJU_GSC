"""
1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.
"""
#1 정수를 두개 입력
a, b = input("정수를 두개 입력: ").split()

#2 정수 바꿈
a = int(a)
b = int(b)

#3 나올 수 있는 모든 경우를 출력
for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(i, j)