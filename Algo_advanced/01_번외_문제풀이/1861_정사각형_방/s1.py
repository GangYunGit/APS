import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 우 하 좌 상
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def bfs(x, y):
    global count
    queue.append((x, y))
    count += 1

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and room[nx][ny] == room[x][y] + 1:
                queue.append((nx, ny))
                count += 1

    return count


for test_case in range(1, int(input()) + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    move_info = []
    room_info = []
    for i in range(N):
        for j in range(N):
            queue = []
            count_list = []
            count = 0
            move_info.append(bfs(i, j))
            room_info.append(room[i][j])

    max_move = max(move_info)
    idx_list = []
    for i in range(len(move_info)):
        if move_info[i] == max_move:
            idx_list.append(i)

    min_room = []
    for idx in idx_list:
        min_room.append(room_info[idx])

    print(f'#{test_case} {min(min_room)} {max_move}')
