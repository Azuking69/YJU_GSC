"""
정수 3개를 입력받아 합과 평균을 출력해보자.
"""
#1 정수 3개를 입력
a, b, c = input("정수 3개를 입력: ").split()

#2 합과 평균을 출력
num_a = int(a)
num_b = int(b)
num_c = int(c)

total = num_a + num_b + num_c


avg = total / 3
print(f"{total} {avg:.3}")