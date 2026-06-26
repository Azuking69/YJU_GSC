"""
실수 2개(f1, f2)를 입력받아
f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.
"""
#1 실수 2개를 입력
f1, f2 = input("실수 2개 입력: ").split()

#2 f1을 f2번 거듭제곱한 값을 출력
result = float(f1) ** float(f2)
print(result)