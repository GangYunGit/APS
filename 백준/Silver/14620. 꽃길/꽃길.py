def blossom_point(i, j):
    return [(i, j), (i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]


def get_cost(i, j):
    return ground[i][j] + ground[i - 1][j] + ground[i][j - 1] + ground[i + 1][j] + ground[i][j + 1]


def dfs(i, j):
    global min_cost
    if len(points) == 3:
        total_cost = 0
        blossom = [[0] * n for _ in range(n)]
        for seed_i, seed_j in points:
            total_cost += get_cost(seed_i, seed_j)
            for blossom_i, blossom_j in blossom_point(seed_i, seed_j):
                blossom[blossom_i][blossom_j] = 1

        if sum(map(sum, [blossom[_] for _ in range(n)])) == 15:
            min_cost = min(min_cost, total_cost)
        return

    for row in range(1, n - 1):
        for col in range(1, n - 1):
            if not visited[row][col]:
                visited[row][col] = True
                points.append((row, col))
                dfs(row, col)
                visited[row][col] = False
                points.pop()


n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]

points = []
visited = [[False] * n for _ in range(n)]
count = 0
min_cost = 200 * n * n
dfs(1, 1)
print(min_cost)