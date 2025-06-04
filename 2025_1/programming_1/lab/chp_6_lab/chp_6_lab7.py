"""
높이가 5인 다이아몬드 형태의 별을 출력
"""
line = 9
#1 위에 별 만들기
for i in range(1, line + 1, 2):
    print(" " * ((line - i) // 2) +  ("*" * i))

#2 밑에 별 만들기
for i in range(line -2, 0, -2):
    print(" " * ((line - i) // 2) +  ("*" * i))