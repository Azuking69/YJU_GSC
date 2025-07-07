"""
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
"""
#1 2개의 정수값이 입력
a, b = input("2개의 정수값이 입력: ").split()

#2 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력
num_a = int(a)
num_b = int(b)

print(not(num_a or num_b))