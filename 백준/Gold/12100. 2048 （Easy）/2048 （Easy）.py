from copy import deepcopy

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def move_row(board, direction):
    start_point, iter_val = 0, 0
    new_board = [[0] * n for _ in range(n)]
    if direction == 0:
        start_point = 0
        iter_val = 1
    elif direction == 2:
        start_point = n - 1
        iter_val = -1

    for col in range(n)[::iter_val]:
        merge_queue = []
        merged_row = start_point
        row = start_point
        while True:
            if row >= n or row < 0:
                if merge_queue:
                    new_board[merged_row][col] = board[merge_queue[0]][col]
                break

            if board[row][col] != 0:
                merge_queue.append(row)

            if len(merge_queue) == 2:
                row1, row2 = merge_queue
                if board[row1][col] == board[row2][col]:
                    new_board[merged_row][col] = board[row1][col] * 2
                    merged_row += iter_val
                    merge_queue = []
                else:
                    new_board[merged_row][col] = board[row1][col]
                    merged_row += iter_val
                    merge_queue.pop(0)
            row += iter_val

    return new_board


def move_col(board, direction):
    start_point, iter_val = 0, 0
    new_board = [[0] * n for _ in range(n)]
    if direction == 3:
        start_point = 0
        iter_val = 1
    elif direction == 1:
        start_point = n - 1
        iter_val = -1

    for row in range(n)[::iter_val]:
        merge_queue = []
        merged_col = start_point
        col = start_point
        while True:
            if col >= n or col < 0:
                if merge_queue:
                    new_board[row][merged_col] = board[row][merge_queue[0]]
                break

            if board[row][col] != 0:
                merge_queue.append(col)

            if len(merge_queue) == 2:
                col1, col2 = merge_queue
                if board[row][col1] == board[row][col2]:
                    new_board[row][merged_col] = board[row][col1] * 2
                    merged_col += iter_val
                    merge_queue = []
                else:
                    new_board[row][merged_col] = board[row][col1]
                    merged_col += iter_val
                    merge_queue.pop(0)
            col += iter_val

    return new_board


def move(board, current_moved):
    global max_val
    if current_moved == 5:
        max_val = max(max_val, max(map(max, board)))
        return

    for direction in range(4):
        prev_board = deepcopy(board)
        if direction == 0 or direction == 2:
            board = move_row(board, direction)
        else:
            board = move_col(board, direction)
        move(board, current_moved + 1)
        board = prev_board


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_val = 0
move(board, 0)
print(max_val)