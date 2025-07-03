"""
정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
"""
#1 정수 2개 입력
a, b = input("정수 2개를 입력: ").split()

#2 a를 b로 나눈 나마지를 출력
result = int(a) % int(b)
print(result)