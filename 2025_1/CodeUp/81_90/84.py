"""
녹음할 시간(초) s가 주어질 때, 필요한 저장 용량을 계산하는 프로그램을 작성해보자.

"""
#1 h, b, c, s 가 공백을 두고 입력
h, b, c, s = input("공백을 두고 입력: ").split()

#2 숫자로 변환
h = int(h)
b = int(b)
c = int(c)
s = int(s)

#3 필요한 저장 공간을 MB 단위로 바꾸어 출력
result = (((h * b * c * s) / 8) / 1024) / 1000

#4 출력
print(f"{result:.1f} MB")