"""
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
"""
#1 10진수를 입력
input_num = int(input("10진수를 입력: "))

#2 16진수로 출력
print('%x'% input_num)
print(f"{input_num:x}") #推奨