"""
사용자에게 리스트 10개를 입력받고, 다양한 조건에 맞게 리스트의 일부분을 
슬라이싱하여 출력하는 프로그램을 작성
"""
#1 사용자에게 리스트 10개를 입력받는다
count = 1
num_list = []
for i in range(10):
    input_num = int(input(f"{count}번째 숫자를 입력하세요: "))
    num_list.append(input_num)
    count += 1
print(f"입력된 리스트: {num_list}")

#2 짝수 인덱스만 출력
even_num = []
for i in range(0, 10, 2):
    even_num.append(num_list[i])
print(f"짝수 인덱스 요소: {even_num}")

#3 홀수 인덱스만 출력
odd_num = []
for i in range(1, 10, 2):
    odd_num.append(num_list[i])
print(f"홀수 인덱스 요소: {odd_num}")

#4 가운데 4개 요소
center_num = []
for i in range(3, 7):
    center_num.append(num_list[i])
print(f"가운데 4개 요소: {center_num}")

#5 마지막 5개를 거꾸로 출력
final_5_num = []
for i in range(9, 4, -1):
    final_5_num.append(num_list[i])
print(f"마지막 5개 역순: {final_5_num}")