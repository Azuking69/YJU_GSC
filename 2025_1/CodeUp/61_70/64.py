"""
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.
"""
#1 세 정수 입력
a, b, c = input("세 정수 입력: ").split()

#2 가장 작은 값을 출력
num_a = int(a)
num_b = int(b)
num_c = int(c)

result = (num_a if (num_a > num_b) else num_b) if ((num_a if num_a > num_b else num_b) > num_c) else num_c

print(result)