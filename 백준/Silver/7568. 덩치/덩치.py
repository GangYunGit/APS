n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
rank = [1] * n

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            rank[i] += 1
print(*rank)