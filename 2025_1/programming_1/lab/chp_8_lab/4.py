"""
세 개의 숫자를 매개변수로 받아 가장 큰 수를 반환하는 함수 max_of_three를작성
"""
# 함수 정의(최대 값을 반환하는 알고리즘은 직접 작성 할 것! max() 함수 사용 금지)
def max_of_three(a, b, c):
    max_val = a
    if max_val < b:
        max_val = b
    elif max_val < c:
        max_val = c
    # 함수에 가져가는다
    return max_val

# 출력: 20
print(max_of_three(10, 20, 15))