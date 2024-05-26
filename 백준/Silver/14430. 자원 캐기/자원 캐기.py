n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dp[0][0] += area[0][0]

for i in range(1, m):
    dp[0][i] = dp[0][i - 1] + area[0][i]
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + area[i][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(area[i][j] + dp[i - 1][j], area[i][j] + dp[i][j - 1])

print(dp[n - 1][m - 1])