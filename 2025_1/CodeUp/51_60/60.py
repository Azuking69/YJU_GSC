"""
입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)
"""
#1 정수 정수 두 개를 입력
a, b = input("정수 두 개를 입력: ").split()

#2 비트단위로 and 연산한 후 그 결과를 정수로 출력
num_a = int(a)
num_b = int(b)

total = num_a + num_b

print(num_a & num_b)