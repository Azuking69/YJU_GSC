"""
리스트와 타겟 숫자를 매개변수로 받아, 타겟 숫자가 리스트 내에 있는지
여부를 반환하는 함수 contains를 작성
"""
# 함수 정의
def contains(num_list, num):
    # 처음 index
    index = 0
    # 검사 횟수
    while index < len(num_list):
        # "True"시
        if num_list[index] == num:
            return "True"
        # 다음 index
        index += 1
    # "False"시("True"이외)
    return "False"

# 출력: True
print(contains([1, 2, 3, 4], 3))
# 출력: False
print(contains([1, 2, 3, 4], 8))