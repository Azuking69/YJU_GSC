#1-1000의 리스트를 작성
numbers_list =  list(range(1,1001))
"""
#확인
print(numbers_list)"
"""
#리스트 중에 있는 3의 배수를 찾아기
count3_number = [num for num in numbers_list if num % 3 == 0]

#출력
print(sum(count3_number))

