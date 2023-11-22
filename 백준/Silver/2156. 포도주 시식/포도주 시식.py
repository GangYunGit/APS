n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = wine[0]
    elif i == 1:
        dp[i] = wine[0] + wine[1]
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

print(dp[-1])