# 11047_동전0
N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]
count = 0

for i in range(N - 1, -1, -1):
    if coin_list[i] <= K:
        count += K // coin_list[i]
        K %= coin_list[i]
        if K == 0:
            break

print(count)
