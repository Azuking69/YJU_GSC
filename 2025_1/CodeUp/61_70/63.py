"""
입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.
"""
#1 정수 두개 입력
a, b = input("정수 두개 입력: ").split()

#2 정수형 변환
num_a = int(a)
num_b = int(b)

#3 큰 값을 출력
result = (num_a if (num_a > num_b) else num_b)
print(result)