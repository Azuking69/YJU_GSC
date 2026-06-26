"""

"""
#1 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력
maze = [list(map(int, input("미로 상자의 구조와 먹이의 위치가 입력: ").split())) for _ in range(10)]

#2 성실한 개미가 이동한 경로를 9로 표시해 출력
x, y = 1, 1

while True:
    # 현재 위치가 먹이(2)거나, 끝(막힘)나기 전까지
    if maze[x][y] == 0:
        maze[x][y] = 9
    elif maze[x][y] == 2:
        maze[x][y] = 9
        break

    # 오른쪽으로 갈 수 있으면
    if maze[x][y + 1] != 1:
        y += 1
    # 오른쪽 못 가면 아래로
    elif maze[x + 1][y] != 1:
        x += 1
    # 둘 다 못 가면 끝
    else:
        break

# 3. 결과 출력
for row in maze:
    print(' '.join(map(str, row)))