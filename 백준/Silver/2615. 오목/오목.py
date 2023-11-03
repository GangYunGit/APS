di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]


def omok(i, j, color):
    for direction_list in [[0, 4], [1, 5], [2, 6], [3, 7]]:
        count = [(i, j)]
        for direction in direction_list:
            ni, nj = i + di[direction], j + dj[direction]
            while True:
                if not (0 <= ni < 19 and 0 <= nj < 19):
                    break
                if board[ni][nj] != color:
                    break
                if board[ni][nj] == color:
                    count.append((ni, nj))
                ni = ni + di[direction]
                nj = nj + dj[direction]

        if len(count) == 5:
            a, b = sorted(count, key=lambda x: x[1])[0]
            return a + 1, b + 1, color

    return -1, -1, color


board = [list(map(int, input().split())) for _ in range(19)]
result = 0
result_i, result_j = -1, -1

for i in range(19):
    for j in range(19):
        if board[i][j] > 0:
            win_i, win_j, win_color = omok(i, j, board[i][j])
            if win_i == -1 and win_j == -1:
                continue
            else:
                result = win_color
                result_i, result_j = win_i, win_j
                break
    if result != 0:
        break

print(result)
if result > 0:
    print(result_i, result_j)