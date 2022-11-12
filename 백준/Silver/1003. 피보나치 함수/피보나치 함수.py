dp = [0 for _ in range(42)]
dp[0] = 1

for i in range(2, 42):
    dp[i] = dp[i - 2] + dp[i - 1]

for test_case in range(1, int(input()) + 1):
    n = int(input())
    print(dp[n], dp[n + 1])