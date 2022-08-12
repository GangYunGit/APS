#  1210_Ladder 1
import sys
sys.stdin = open("input.txt")

dx = [0, 0, -1]  # ----- 상 하
dy = [-1, 1, 0]  # 좌 우 -----

for test_case in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    x_end, y_end = 0, 0

    # 도착지점의 좌표를 찾는 반복문
    for x in range(100):
        for y in range(100):
            if ladder[x][y] == 2:
                x_end = x
                y_end = y

    # 방향 탐색
    direction = -1
    while x_end != 0:
        direction = (direction + 1) % 3  # 나머지 연산을 이용, 특정 지점에서 3방향을 탐색
        nx = x_end + dx[direction]  # 다음x 방향
        ny = y_end + dy[direction]  # 다음y 방향

        if 0 <= nx <= 99 and 0 <= ny <= 99: # 사다리의 범위를 넘어서는 좌표 제외
            if ladder[nx][ny] == 1: # 1이 있는 곳을 검색
                x_end = nx  # 현재 x의 좌표 최신화
                y_end = ny  # 현재 y의 좌표 최신화
                ladder[nx][ny] = 0  # 지나온 곳은 0으로 표시하여 무한루프에 빠지는 것을 방지

    print(f'#{T} {y_end}')


