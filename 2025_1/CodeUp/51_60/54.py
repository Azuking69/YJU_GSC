"""
2개의 정수값이 입력될 때,
그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
"""
#1 2개의 정수값이 입력
a, b = input("2개의 정수값이 입력: ").split()

#2 int형 변환
num_a = int(a)
num_b = int(b)

#3 그 불 값이 모두 True 일 때에만 True
print(bool(num_a) and bool(num_b))