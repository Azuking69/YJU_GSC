"""
가변 개수의 숫자를 매개변수로 받아 평균을 반환하는 함수
calculate_average를 작성
"""
#1 정의
#2 가변변수를 사용
def calculate_average(*list_num):
    #3 변수 초기화
    sum = 0
    for num in list_num:
        sum += num
        avg = sum / len(list_num)
        return avg

# 출력
print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))