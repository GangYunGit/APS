import sys
input = sys.stdin.readline

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]


def dfs(i, j, p, start, end):
    global result

    if (i, j) in route:
        result += p
        route.append((i, j))
        return

    route.append((i, j))

    if start == end:
        return

    for direction in range(4):
        next_i = i + di[direction]
        next_j = j + dj[direction]
        if 0 <= next_i < 31 and 0 <= next_j < 31:
            dfs(next_i, next_j, p * p_list[direction], start + 1, end)
            route.pop()


move, east, west, north, south = map(int, input().split())
p_list = [east / 100, west / 100, north / 100, south / 100]
board_size = 2 * move + 1
board = [[0] * board_size for _ in range(board_size)]
i, j = move, move
result = 0
route = []
dfs(i, j, 1, 0, move)
print(1 - result)