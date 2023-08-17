import sys

input = sys.stdin.readline

freedom = int(input())
meeting = [list(map(int, input().split())) for _ in range(freedom)]
dp = [0] * (freedom + 1)

for day in range(freedom - 1, -1, -1):
    if day + meeting[day][0] > freedom:
        dp[day] = dp[day + 1]

    else:
        compare = dp[day + meeting[day][0]] + meeting[day][1]
        if compare > dp[day + 1]:
            dp[day] = compare
        else:
            dp[day] = dp[day + 1]

print(max(dp))