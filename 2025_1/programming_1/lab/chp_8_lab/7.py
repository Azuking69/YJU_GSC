"""
리스트와 타겟 숫자를 매개변수로 받아, 타겟 숫자가 리스트 내에 있는지
여부를 반환하는 함수 contains를 작성
"""
#1 정의
def contains(a_list, b):
    #2 처음 index
    i = 0
    while i < len(a_list):
        if a_list[i] == b:
            return "True"
        #3 다음 index
        i += 1
    return "False"

#4 출력
print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))