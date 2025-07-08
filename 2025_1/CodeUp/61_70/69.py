"""
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A   : best!!!
B   : good!!
C   : run!
D   : slowly~
나머지 문자들 : what?
"""
#1 평가를 문자로 입력
word = input("평가를 문자로 입력: ")

#2 내용을 다르게 출력
if word == "A":
    print("best!!!")
elif word == "B":
    print("good!!")
elif word == "C":
    print("run!")
elif word == "D":
    print("slowly~")
else:
    print("what?")