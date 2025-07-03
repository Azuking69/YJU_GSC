"""
정수 2개(a, b)를 입력받아
a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
"""
#1 정수 2개(a, b)를 입력
num1, num2 = input("정수 2개를 입력: ").split()

#2 a를 b번 곱한 거듭제곱을 출력
result = int(num1) ** int(num2)
print(result)