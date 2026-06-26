"""
정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.
"""
#1 정수 2개(a, b)를 입력
num1, num2 = input("정수 2개(a, b)를 입력: ").split()


#2 a에서 b를 뺀 차를 출력
result = int(num1) - int(num2)
print(result)