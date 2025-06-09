"""
세 개의 숫자를 매개변수로 받아 가장 큰 수를 반환하는 함수 max_of_three를작성
"""
#1 아래와 같이 출력 되도록 함수를 정의
def max_of_three(a, b, c):
    #2 최대 값을 반환하는 알고리즘은 직접 작성 할 것! max() 함수 사용 금지
    max_of_three = a
    if max_of_three < b:
        max_of_three = b
    elif max_of_three < c:
        max_of_three = c
    return max_of_three

#3 출력
print(max_of_three(10, 20, 15))