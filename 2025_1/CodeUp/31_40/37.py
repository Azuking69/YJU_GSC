"""
반복 횟수와 문장을 입력받아 여러 번 출력해보자.
"""
#1 반복 횟수와 문장을 입력
count = int(input("횟수를 입력: "))
word = input("문장을 입력: ")

#2 여러 번 출력
for _ in range(count):
    print(word, end=" ")