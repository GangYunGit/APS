import sys
input = sys.stdin.readline

n = int(input())
word = list(map(int, input().split()))
m = int(input())
question = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n - i):
        s, e = j, i + j
        if word[s] == word[e]:
            if i < 2:
                dp[s][e] = 1
            elif dp[s + 1][e - 1] == 1:
                dp[s][e] = 1

for s, e in question:
    print(dp[s - 1][e - 1])