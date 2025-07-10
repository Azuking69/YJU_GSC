"""
1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
3의 배수인 경우는 출력하지 않도록 만들어보자.
"""
#1 정수 입력
num = int(input("정수 입력: "))

#2 3의 배수인 경우는 출력하지 않다
for i in range(num + 1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=" ")