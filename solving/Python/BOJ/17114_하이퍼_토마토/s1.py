# BOJ_17114. 하이퍼 토마토

from collections import deque

d1 = [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d2 = [0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d3 = [0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d4 = [0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d5 = [0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
d9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0]
d10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0]
d11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0]
d12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1]


def bfs(tomatoes):
    global depth
    # queue = deque()
    # for (k, i, j) in tomatoes:
    #     visited[k][i][j] = True
    #     queue.append((k, i, j, depth))
    #
    # while queue:
    #     temp_k, temp_i, temp_j, depth = queue.popleft()
    #
    #     for direction in range(6):
    #         next_k = temp_k + dk[direction]
    #         next_i = temp_i + di[direction]
    #         next_j = temp_j + dj[direction]
    #         if 0 <= next_k < height and 0 <= next_i < row and 0 <= next_j < col and not visited[next_k][next_i][next_j] and box[next_k][next_i][next_j] != -1:
    #             visited[next_k][next_i][next_j] = True
    #             box[next_k][next_i][next_j] = 1
    #             queue.append((next_k, next_i, next_j, depth + 1))

    return depth


direction = list(map(int, input().split()))
rows = 1
for i in direction[1:]:
    rows *= i

box = [list(map(int, input().split())) for _ in range(rows)]
print(box)

visited = [[False] * direction[0] for _ in range(rows)]
tomatoes = []
not_cooked_count = 0

for i1 in range(direction[0]):
    for i2 in range(direction[1]):
        for i3 in range(direction[2]):
            for i4 in range(direction[3]):
                for i5 in range(direction[4]):
                    for i6 in range(direction[5]):
                        for i7 in range(direction[6]):
                            for i8 in range(direction[7]):
                                for i9 in range(direction[8]):
                                    for i10 in range(direction[9]):
                                        for i11 in range(direction[10]):
                                            for i12 in range(direction[11]):
                                                if box[i1][i1] == 1:
                                                    tomatoes.append((k, i, j))
                                                if box[k][i][j] == 0:
                                                    not_cooked_count += 1

if not_cooked_count == 0:
    print(0)
else:
    depth = 0
    bfs(tomatoes)
    for i1 in range(direction[0]):
        for i2 in range(direction[1]):
            for i3 in range(direction[2]):
                for i4 in range(direction[3]):
                    for i5 in range(direction[4]):
                        for i6 in range(direction[5]):
                            for i7 in range(direction[6]):
                                for i8 in range(direction[7]):
                                    for i9 in range(direction[8]):
                                        for i10 in range(direction[9]):
                                            for i11 in range(direction[10]):
                                                for i12 in range(direction[11]):
                                                    if box[i1][i2][i3][i4][i5][i6][i7][i8][i9][i10][i11][i12] == 0:
                                                        print(-1)
                                                        exit()
    print(depth)
