import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(i, j, count):
    global max_count
    max_count = max(max_count, count)
    alphabet_list[ord(board[i][j]) - 65] = True

    for direction in range(4):
        check_i = i + di[direction]
        check_j = j + dj[direction]

        if (
                0 <= check_i < row and 0 <= check_j < col
                and board[check_i][check_j]
                and not alphabet_list[ord(board[check_i][check_j]) - 65]
        ):
            dfs(check_i, check_j, count + 1)

    alphabet_list[ord(board[i][j]) - 65] = False
    count -= 1


row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]

alphabet_list = [False] * 26
max_count = 0
dfs(0, 0, 1)

print(max_count)