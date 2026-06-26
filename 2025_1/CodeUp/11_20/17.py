"""
정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 
한 줄로 3번 출력해보자.
"""

#1 정수, 실수, 문자, 문자열 등 1개만 입력
input_som = input("1개만 입력: ")

#2 한 줄로 3번 출력
for _ in range(3):
    print(input_som, end=" ")
