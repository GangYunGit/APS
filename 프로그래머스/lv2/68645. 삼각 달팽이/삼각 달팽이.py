di = [1, 0, -1]
dj = [0, 1, -1]


def solution(n):
    def dfs(i, j):
        direction = 0
        for count in range(1, n * (n + 1) // 2 + 1):
            arr[i][j] = count
            next_i = i + di[direction]
            next_j = j + dj[direction]
            if 0 <= next_i < n and 0 <= next_j < n and arr[next_i][next_j] == 0:
                i = next_i
                j = next_j
            else:
                direction = (direction + 1) % 3
                i += di[direction]
                j += dj[direction]

    arr = [[0] * n for _ in range(n)]

    dfs(0, 0)
    answer = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                answer.append(arr[i][j])

    return answer