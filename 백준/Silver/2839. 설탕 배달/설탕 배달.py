n = int(input())
dp = [-1 for _ in range(n + 1)]

for i in range(3, n + 1):
    if i == 3:
        dp[i] = 1
    if i == 5:
        dp[i] = 1

    if dp[i - 3] != -1:
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != -1:
        dp[i] = dp[i - 5] + 1

print(dp[n])