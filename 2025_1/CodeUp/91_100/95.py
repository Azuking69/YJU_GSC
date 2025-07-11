"""
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
"""
#1 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력
while True:
    n = int(input("흰 돌의 개수를 입력: "))
    if n < 0 or n > 19:
        continue

    #2 바둑판 만들기
    else:
        d = []
        for _ in range(20):
            d.append([0] * 20)

    #3 둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력
        for i in range(n):
            x, y = input("좌표 입력: ").split()
            d [int(x) - 1][int(y) - 1] = 1

    #4 흰 돌이 올려진 바둑판의 상황을 출력
        for i in range(20):
            for j in range(20):
                print(d[i][j], end=" ")

            #5 흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력
            print()
        break