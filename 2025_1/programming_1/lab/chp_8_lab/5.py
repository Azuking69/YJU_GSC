"""
주어진 수가 짝수인지 홀수인지 판별하는 함수 is_even을 작성
"""
# 함수 정의
def is_even(num):
    # 짝수
    if num % 2 == 0:
        return "True"
    # 홀수
    else:
        return "False"

#출력: True
print(is_even(4))
#출력: False
print(is_even(5))