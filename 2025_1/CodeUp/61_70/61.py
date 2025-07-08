"""
입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.
"""
#1 정수 입력
a, b = input("정수 두 개 입력: ").split()

#2 비트단위로 or 연산
num_a = int(a)
num_b = int(b)

total = num_a | num_b

#3 결과를 정수로 출력
print(int(total))