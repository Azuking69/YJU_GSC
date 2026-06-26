"""
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단, b는 0이 아니다.
"""
#1 정수 2개(a, b)를 입력
a, b = input("정수 2개를 입력: ").split()

#2 정수 변화
num_a = int(a)
num_b = int(b)

#3 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산
print(num_a + num_b)
print(num_a - num_b)
print(num_a * num_b)
print(f"{int(num_a / num_b)}")
print(num_a % num_b)
print(f"{(num_a / num_b):.3}")