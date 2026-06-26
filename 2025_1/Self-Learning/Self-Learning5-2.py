"""
자연수 N을 입력 받아서, 지정된 패턴으로 별(*)을 출력
"""

#입력
input_number = int(input("N 입력: "))

#별 만들기
for i in range(1, input_number):
    print("*" * i)

for i in range(input_number, 0 , -1):
    print("*" * i)