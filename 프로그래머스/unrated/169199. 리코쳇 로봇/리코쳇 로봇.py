from collections import deque

def solution(board):
    answer = 0
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    row_size = len(board)
    col_size = len(board[0])

    def bfs(i, j):
        visited = [[False] * col_size for _ in range(row_size)]
        queue = deque()
        queue.append((i, j, 0))
        visited[i][j] = True
        
        while queue:
            i, j, count = queue.popleft()
            if board[i][j] == 'G':
                return count
            
            for direction in range(4):
                next_i = i + di[direction]
                next_j = j + dj[direction]
                stop_i, stop_j = 0, 0
                while True:
                    if not(0 <= next_i < row_size and 0 <= next_j < col_size) or board[next_i][next_j] == 'D':
                        stop_i, stop_j = next_i - di[direction], next_j - dj[direction]
                        break
                    next_i += di[direction]
                    next_j += dj[direction]
                
                if not visited[stop_i][stop_j]:
                    visited[stop_i][stop_j] = True
                    queue.append((stop_i, stop_j, count + 1))
                
        return - 1
        
        
    for i in range(row_size):
        for j in range(col_size):
            if board[i][j] == 'R':
                answer = bfs(i, j)
        
    return answer