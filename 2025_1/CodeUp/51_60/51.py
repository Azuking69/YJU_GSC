"""
두 정수(a, b)를 입력받아 a의 값이 b의 값과 서로 다르면 True 를, 
같으면 False 를 출력하는 프로그램을 작성
"""
#1 두 정수(a, b)를 입력
a, b = input("두 정수(a, b)를 입력: ").split()

#2 a의 값이 b의 값과 서로 다르면 True, 같으면 False 를 출력
num_a = int(a)
num_b = int(b)

print(num_a != num_b)