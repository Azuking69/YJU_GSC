"""
While문을 사용하여 1~1000까지의 정수 중 3의배수의 총합을 구하라
"""
#1 1~1000까지의 정수 
num_list = list(range(1, 1000 + 1))

#2 변수 초기화
i = 0
total = 0

#3 while문을 사용하여 3의 배수의 합 계산
while i < len(num_list): #len()로 num_list요소 개수를 확인
    if num_list[i] % 3 == 0:
        total += num_list[i]
    i += 1

#4 결과 출력
print("1~1000 사이 정수 중 3의 배수의 총 합은 :", total)