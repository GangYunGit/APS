# 상 우 하 좌 우상 우하 좌하 좌상
di = [-1, 0, 1, 0, 1, -1, -1, 1]
dj = [0, 1, 0, -1, 1, 1, -1, -1]


def put_stone(i, j, color):

    board[i][j] = color
    for k in range(8):
        radius = 1
        next_i = i + radius * di[k]
        next_j = j + radius * dj[k]

        while 0 <= next_i < board_size and 0 <= next_j < board_size and board[next_i][next_j] == 3 - color:
            radius += 1
            next_i = i + radius * di[k]
            next_j = j + radius * dj[k]

        if 0 <= next_i < board_size and 0 <= next_j < board_size and board[next_i][next_j] == color:
            for r in range(1, radius):
                board[i + r * di[k]][j + r * dj[k]] = color


for test_case in range(1, int(input()) + 1):
    board_size, rounds = map(int, input().split())
    stone_info = [list(map(int, input().split())) for _ in range(rounds)]

    # 흑돌 = 1, 백돌 = 2
    board = [[0] * board_size for _ in range(board_size)]
    board[board_size // 2 - 1][board_size // 2 - 1] = 2
    board[board_size // 2][board_size // 2] = 2
    board[board_size // 2][board_size // 2 - 1] = 1
    board[board_size // 2 - 1][board_size // 2] = 1

    for col, row, color in stone_info:
        put_stone(row - 1, col - 1, color)

    black_count = 0
    white_count = 0
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 1:
                black_count += 1
            elif board[row][col] == 2:
                white_count += 1

    print(f'#{test_case} {black_count} {white_count}')
