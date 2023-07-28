from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(start_puzzle):
    visited = set()
    queue = deque()
    queue.append((start_puzzle, 0))
    while queue:
        temp_puzzle, depth = queue.popleft()
        if temp_puzzle == sorted_puzzle:
            return depth

        temp_idx = temp_puzzle.index('0')
        i, j = temp_idx // 3, temp_idx % 3
        for direction in range(4):
            check_i, check_j = i + di[direction], j + dj[direction]
            if 0 <= check_i < 3 and 0 <= check_j < 3:
                next_idx = check_i * 3 + check_j
                new_puzzle = list(temp_puzzle)
                new_puzzle[temp_idx], new_puzzle[next_idx] = new_puzzle[next_idx], new_puzzle[temp_idx]
                next_puzzle = ''.join(new_puzzle)
                if next_puzzle not in visited:
                    visited.add(next_puzzle)
                    queue.append((next_puzzle, depth + 1))

    return -1


puzzle = [list(map(int, input().split())) for _ in range(3)]

sorted_puzzle = '123456780'
start_puzzle = ''
for i in range(3):
    for j in range(3):
        start_puzzle += str(puzzle[i][j])
print(bfs(start_puzzle))