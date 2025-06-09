"""
주어진 수가 짝수인지 홀수인지 판별하는 함수 is_even을 작성
"""

#1 함수 정의
def is_even(num):
    if num % 2 == 0:
        return "True"
    else:
        return "False"

#2 출력
print(is_even(4))
print(is_even(5))