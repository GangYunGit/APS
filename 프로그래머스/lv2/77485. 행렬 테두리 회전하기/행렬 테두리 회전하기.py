from collections import deque


def solution(rows, columns, queries):
    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    board = [[] for _ in range(rows)]
    answer = []
    for i in range(rows):
        for j in range(1, columns + 1):
            board[i].append(i * columns + j)

    for point in queries:
        direction = 0
        queue = deque()
        start_i, start_j = point[0] - 1, point[1] - 1
        queue.append(board[start_i][start_j])
        next_board = board[start_i][start_j]
        while not(start_i == point[0] and start_j == point[1] - 1):
            if start_i == point[0] - 1 and start_j == point[3] - 1:
                direction = 1
            elif start_i == point[2] - 1 and start_j == point[3] - 1:
                direction = 2
            elif start_i == point[2] - 1 and start_j == point[1] - 1:
                direction = 3
            start_i += di[direction]
            start_j += dj[direction]
            queue.append(board[start_i][start_j])

        queue.rotate(1)
        direction = 0
        idx = 0
        start_i, start_j = point[0] - 1, point[1] - 1
        board[start_i][start_j] = queue[idx]
        new_list = [queue[idx]]
        while not(start_i == point[0] and start_j == point[1] - 1):
            idx += 1
            if start_i == point[0] - 1 and start_j == point[3] - 1:
                direction = 1
            elif start_i == point[2] - 1 and start_j == point[3] - 1:
                direction = 2
            elif start_i == point[2] - 1 and start_j == point[1] - 1:
                direction = 3
            start_i += di[direction]
            start_j += dj[direction]
            board[start_i][start_j] = queue[idx]
            new_list.append(queue[idx])
        answer.append(min(new_list))
    return answer