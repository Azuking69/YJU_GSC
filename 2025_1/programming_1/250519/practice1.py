"""
 사용자로부터 받은 리스트에서 다양한 슬라이싱 방법으로 부분 리스트를 생성
"""

#1 사용자로부터 정수 10개를 입력받아
print("정수를 입력하세요.")
num_list = []

#2 리스트 data 생성
for i in range(10):
    num = int(input(f"{i + 1}번째 정수: "))
    num_list.append(num)

#3 처음 5개 원소
print(f"1.처음 5개 원소: {num_list[0 : 5]}")
#4 뒤에서 3개 원소
print(f"2.뒤에서 3개 원소: {num_list[-1 : -3 -1 : -1]}")
#5 짝수 인덱스 원소만 추출
print(f"3.짝수 인덱스 원소만 추출: {num_list[0 : 10 + 1 : 2]}")
#6 리스트를 거꾸로 뒤집(逆にひっくり返す)은 결과
print(f"1.리스트를 거꾸로 뒤집은 결과: {num_list[-1 : -10 -1 : -1]}")