"""
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
"""
#1 영문 소문자(a ~ z) 1개가 입력
word = ord(input("영문 소문자 1개가 입력: "))

#2 a부터 그 문자까지의 알파벳을 순서대로 출력
# a를 정수에 바꿈
start = ord("a")

# while문으로 반복
while start <= word:
    print(chr(start), end=" ")
    start += 1