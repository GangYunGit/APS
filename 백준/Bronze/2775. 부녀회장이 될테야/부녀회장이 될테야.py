for _ in range(int(input())):
    dp = [i for i in range(1, 15)]
    k, n = int(input()), int(input())
    for i in range(k):
        for j in range(13, -1, -1):
            dp[j] = sum(dp[:j + 1])
    print(dp[n - 1])
