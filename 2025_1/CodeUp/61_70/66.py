"""
3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
"""
#1 3개의 정수 입력
a, b, c = input("3개의 정수 입력: ").split()

#2 int형 변환
a = int(a)
b = int(b)
c = int(c)

#3 짝(even)/홀(odd)을 출력
if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")

if c % 2 == 0:
    print("even")
else:
    print("odd")