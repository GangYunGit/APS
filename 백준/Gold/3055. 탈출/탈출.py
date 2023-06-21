from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(points):
    visited_water = [[False] * col for _ in range(row)]
    visited_hedgehog = [[False] * col for _ in range(row)]
    queue = deque()
    depth = 1
    for i, j, item_type in points:
        queue.append((i, j, item_type, depth))

    while queue:
        i, j, item_type, depth = queue.popleft()

        for direction in range(4):
            ni = i + di[direction]
            nj = j + dj[direction]
            if 0 <= ni < row and 0 <= nj < col:
                if forest[ni][nj] != 'X':
                    if item_type == '*':
                        if forest[ni][nj] == 'D':
                            continue
                        if not visited_water[ni][nj]:
                            visited_water[ni][nj] = True
                            forest[ni][nj] = '*'
                            queue.append((ni, nj, '*', depth))
                    else:
                        if not visited_hedgehog[ni][nj]:
                            visited_hedgehog[ni][nj] = True
                            if forest[ni][nj] == 'D':
                                return depth
                            if forest[ni][nj] == '*':
                                continue
                            forest[ni][nj] = 'S'
                            queue.append((ni, nj, 'S', depth + 1))

    return -1


row, col = map(int, input().split())
forest = [" ".join(input()).split() for _ in range(row)]
points = []
start_point = ()
end_point = ()

for i in range(row):
    for j in range(col):
        if forest[i][j] == '*':
            points.append((i, j, '*'))
        elif forest[i][j] == 'S':
            start_point = (i, j, 'S')
        elif forest[i][j] == 'D':
            end_point = (i, j, 'D')

points.append(start_point)
result = bfs(points)
if result == -1:
    print("KAKTUS")
else:
    print(result)