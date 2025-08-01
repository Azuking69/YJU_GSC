"""
정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 
원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.
"""
#2 길이가 11 이상이면 리스트에 있는 모든 원소의 합
def solution(my_list):

    if len(my_list) >= 11:
        return sum(my_list)
        
    #3 10 이하이면 모든 원소의 곱
    elif len(my_list) <= 10:
        result = 1
        for i in my_list:
            result *= i
        return result
    

#1 list 정의
my_list = list(map(int, input("리스트 저수 입력: ").split(',')))

#4 출력
print(solution(my_list))