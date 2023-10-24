k = int(input())
dp = [1, 0, 1] + [0] * (k - 1)

for i in range(3, k + 2):
    dp[i] = dp[i - 1] + dp[i - 2]
print(*dp[-2::])