"""
단어와 반복 횟수를 입력받아 여러 번 출력해보자.
"""
#1 단어와 반복 횟수를 입력
word, count = input("단어와 반복 횟수를 입력: ").split()

#2 여러 번 출력
for _ in range(int(count)):
    print(word, end="")