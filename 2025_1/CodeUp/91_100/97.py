"""
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
"""
#1 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력
h, w = input("첫 줄에 격자판의 세로, 가로 가 공백을 두고 입력: ").split()
h = int(h)
w = int(w)

#2 두 번째 줄에 놓을 수 있는 막대의 개수(n) 입력
n = int(input("두 번째 줄에 놓을 수 있는 막대의 개수 입력: "))

board = [[0] * w for _ in range(h)]
for _ in range(n):
    #3 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력
    l, d, x, y = input("세 번째 줄부터 각 막대의 길이, 방향, 좌표 입력: ").split()
    l = int(l)
    d = int(d)
    x = int(x) - 1
    y = int(y) - 1

    #4 모든 막대를 놓은 격자판의 상태를 출력
    for i in range(l):
        if d == 0:
            board[x][y + i] = 1
        else:
            board[x + i][y] = 1

#5 출력
for row in board:
    print(' '.join(map(str, row)))