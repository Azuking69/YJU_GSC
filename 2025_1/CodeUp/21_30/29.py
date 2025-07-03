"""
16진수를 입력받아 8진수(octal)로 출력해보자.
"""
#1 16진수를 입력
input_num = input("16진수를 입력: ")

#2 8진수로 출력
num_16 = int(input_num, 16) #16진수
print(f"{num_16:o}")